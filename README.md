# QSearch
__Idea created by Luke Wharton on 4/5/2024__

This is my attempt at fixing a problamatic problem currently plagueing my life **forgetting file names**, to get around this my great plan is to provide an on machine search engine (everything is done on your laptop to prevent data scraping) for your files.

###  How?

First all document data is ran through an LLM capable of extracting the meaning from each document and vectorizing it, all of these vectored are then stored in a 2d array, [[vector, document], [vector, document] ...].

Second is then the search query, upon which it too is ran through an SBERT algorthym, vectorizing the data, upon which it will be cosine compared with all of the pre-vectored documents, until finding one with the most similarity. 

### Example Use Case

Lets say you have a file named "petcare.txt" aptly named because it details how to take care of a multitude of animals. Now lets also say you have completely forgot the name of this file and are in need of instructions to take care of your turtle. All you would need to do is search something like "How to take care of turtle", and it will appear (given you dont have any other files on taking care of turtles, then they would appear too...)

### Why I think its better than a normal search?

Rather than searching for the word to appear in the file, we are comparing the meaning of a search query to a document, which in my mind should yeild more powerfull and accurate results than a normal search. 
