# data-extraction

Implementing requirements for extracting data from a text file.

This repository provides the following info about a text file given:

1. The amount of lines in the file
2. The amount of words in the file
3. The amount of unique words in the file
4. The average sentence length & maximum sentence length
5. The most popular word in the text & The most popular word which is not a word with a syntactic meaning in English
6. The longest word sequence in a text that does not contain the letter k
7. The names of the people that appear in the text & the one which is most common within the text

**Example**

Given a file example.txt contains the following text:
```
Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger; 
Sanger coined its name as a blending of "wiki" and "encyclopedia". Initially 
available only in English, versions in other languages were quickly developed. Its 
combined editions comprise more than 57 million articles, attracting around 2 billion 
unique device visits per month, and more than 17 million edits per month (1.9 edits per 
second). In 2006, Time magazine stated that the policy of allowing anyone to edit had 
made Wikipedia the "biggest (and perhaps best) encyclopedia in the world", and is "a 
testament to the vision of one man, Jimmy Wales".
```
Run ```main.py``` file
```
Enter file name:
```
Enter ```example.txt```

The result:
```
Number of rows:  8
Number of words: 104
Number of unique words: 79
Average sentence length: 25.75
Max sentence length: 37
Most popular word: and
Most popular meaningful word: Wikipedia
Longest sequence with no 'k':   developed. Its
combined editions comprise more than 57 million articles, attracting around 2 billion
unique device visits per month, and more than 17 million edits per month (1.9 edits per
second). In 2006, Time magazine stated that the policy of allowing anyone to edit had
made
All names existing: Larry Sanger, Sanger, Jimmy Wales
Most popular name: Jimmy Wales
```
