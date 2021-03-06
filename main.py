import parser
import analyzer
import categorize
from solver import solve
from Tkinter import *
from tkFont import Font
import Tkinter as tk1
import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


#ttk.Label(root, text='Attention!', font=appHighlightFont).grid()
def quesList():
    quesno = int(qno.get())
    # Step 2: Simplify the question by resolving conjunctions
    word_problem = parser.parse(questions[quesno])
    question_statement = 'Question: ' + questions[quesno]
    rlabel3 = Label(root, text=question_statement, bg='#FB926B').pack()
    # Step 3 : Extract entities from the question
    owners, quantities, verbs, obj, word_problem = analyzer.extract(word_problem)
    # Step 4: categorize questions based on verb and schema and perform computations
    entities = categorize.assign(owners, verbs, quantities)
    # Step 5: processing the question and answering it
    answer_list = solve(word_problem, entities)
    rlabel5 = Label(root, text=answer_list, bg='#80ddff').pack()
    return


def quesEnter():
    question_text = question.get()
    # Step 2: Simplify the question by resolving conjunctions
    word_problem = parser.parse(question_text)
    print(word_problem)
    question_statement = 'Question: ' + question_text
    rlabel3 = Label(root, text=question_statement, bg='#FB926B').pack()
    # Step 3 : Extract entities from the question
    owners, quantities, verbs, obj, word_problem = analyzer.extract(word_problem)
    print(owners,quantities, verbs, obj , word_problem)
    # Step 4: categorize questions based on verb and schema and perform computations
    entities = categorize.assign(owners, verbs, quantities)
    # Step 5: processing the question and answering it
    answer_list = solve(word_problem, entities)
    rlabel5 = Label(root, text=answer_list, bg='#80ddff').pack()
    return

# Step 1: Read questions from file
def main():
    choice1 = int(choice.get())
    if choice1 == 1:
        temptext = 'Select a question number from this list first!\n\n\n\n'
        # Load questions from file
        for i, q in enumerate(questions):
            temptext += "Question " + str(i) + ": " + q + '\n'
        open_file('data/questions.txt')
        rlabel3 = Label(root, text='\nEnter the question number from the list:',  bg='#EFF493').pack()
        rentry = Entry(root, textvariable=qno, bg='black', fg='white', width=20, justify=CENTER).pack()
        rbutton = Button(root, text="Solve", command=quesList, bg='black', fg='white' , borderwidth=5).pack()
    else:
        rlabel4 = Label(root, text='\nEnter the question: ',  bg='#EFF493').pack()
        rentry2 = Entry(root, textvariable=question,  bg='black', fg='white', width=100, justify=CENTER).pack()
        rbutton2 = Button(root, text="Solve", command=quesEnter, bg='black', fg='white' , borderwidth=5).pack()


#setting up the UI
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
resolution = str(width) + "x" + str(height)
root.configure(background='#EFF493')
appHighlightFont_pos = Font(family='Helvetica', size=10)
appHighlightFont_neg = Font(family='Helvetica', size=10)
appHighlightFont_Topic = Font(family='Comic Sans MS', size=20, weight='bold')
appHighlightFont_Note = Font(family='Helvetica', size=12, weight='bold')
qno = StringVar()
question = StringVar()
choice = StringVar()
root.geometry(resolution)
root.title('Arithmetic Word Problem Solver')

#opening dataset file
with open('data/q2.txt', 'r') as fi:
    word_problem = ''
    questions = fi.readlines()
    rlabel = Label(root, text="CSE 537- Arithmetic Word Problem Solver (List of questions):" , fg='Blue', bg='#EFF493', font = appHighlightFont_Topic).pack()
    rlabel3 = Label(root, text='Do you want to select a question from a preset question list (1) or enter your own (2)? Enter (1 / 2):', bg='#EFF493').pack()
    rentry3 = Entry(root, textvariable=choice, bg='black', fg='white', width=20, justify=CENTER).pack()
    rbutton3 = Button(root, text="Go", command=main, bg='black', fg='white' , borderwidth=5).pack()
    rlabel2 = Label(root,
                    text='Note: If you select option 1, a window with question list will appear. Please close that window after finalizing the question!\n If you want to solve more questions, keep entering your choice in the above text box subsequently!',
                    bg='#EFF493', font=appHighlightFont_Note).pack()
mainloop()
