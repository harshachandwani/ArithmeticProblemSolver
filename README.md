# ArithmeticProblemSolver

Question Answering comprises elements of Information Retrieval and Natural language Processing (NLP). Though the discipline has grown to include a variety of ways to accomplish the task of providing a correct answer to a textual input, the general approach in previous implementations of question answering systems is to query a database which may either be specifically related to the question (closed domain) or a general corpus of natural language documents.

Arithmetic Problem Solving indirectly builds from this general approach.  With the availability of different Natural Language Processing Tools and APIs such as the StanfordCoreNLP package, we are able to focus on the linguistic structure of the problems as well as investigating how the structure may be helpful in returning a correct answer for the arithmetic problem.

During the course of completing this project, we have implemented a number of features that we believe ultimately contribute to the accuracy of the knowledge representations made during the solving of the problem as well as the accuracy of the answer returned. The significant accomplishments are as follows:

1. Conjunction Resolution: This serves to resolve any conjunctions present in the problem by splitting the sentence or sentences containing the conjunctions into separate parts, identifying the subjects present, resolving by copying any missing verbs or subjects and returning two sentences. 
2. Entity Extraction: Here, the entities are represented as class objects with fields corresponding to owner and the quantity of the object in question. For example, the sentence John has 4 books would be represented as an Entity object e, where e.owner = “John” and e.value = “4”. The object in question “book” would also be returned here. 
3. Categorizing Questions: Here the keyword which is a verb in the question is determined. This verb is then used to categorize which dictates what computation should be made and which values should be involved in this computation.
The above represent individual components utilized by the system.

