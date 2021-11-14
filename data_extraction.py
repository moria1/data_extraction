# -*- coding: utf-8 -*-

import re
import spacy 
from collections import Counter

def num_rows(fname):
    with open (fname,'r') as f: 
        row_count = sum(1 for r in f)
    print("Number of rows: ", row_count)

def num_words(fname):
    text = get_text(fname)
    word_count = len(get_words(text))
    print("Number of words:", word_count)
    
def num_unique_words(fname):
    text = get_text(fname)
    u_count = len(set(get_words(text)))
    print("Number of unique words:", u_count)
    
def avg_and_max_sentence_len(fname):
    text = get_text(fname)
    end_sen_pattern = "[\.\?\!][ \n\"] *\n*[A-Z\'\"]"
    sentences = re.split(end_sen_pattern, text)
    sentences_len = [len(s.split()) for s in sentences]
    avg_len = sum(sentences_len) / len(sentences)
    max_len = max(sentences_len)
    print("Average sentence length:", round(avg_len, 2))
    print("Max sentence length:", max_len)

def most_popular_word(fname):
    text = get_text(fname)
    words = get_words(text)
    most_pop_word = Counter(words).most_common(1)
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text[:100000]) #to prevent NER memory allocation errors    
    meaningful_words = [w.text.strip() for w in doc if w.is_alpha and not w.is_stop]
    most_pop_mean = Counter(meaningful_words).most_common(1)
    
    pretty_print_tuple("Most popular word:", most_pop_word)
    pretty_print_tuple("Most popular meaningful word:", most_pop_mean)
    
def longest_no_k_seq(fname):
    text = get_text(fname)
    contains_k_pattern = "\w*[kK]\w*"
    sequences = re.split(contains_k_pattern, text)
    longest = 0
    longest_seq = ""
    for seq in sequences:
        if len(seq) > longest:
            longest = len(seq)
            longest_seq = seq
    print("Longest sequence with no 'k': ", longest_seq)
    
def people_names(fname):
    text = get_text(fname)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text[:100000]) #to prevent NER memory allocation errors
    names = [X.text.strip() for X in doc.ents if  X.label_ == 'PERSON']
    most_popular = Counter(names).most_common(1)
    print("All names existing:", ', '.join(set(names)))
    pretty_print_tuple("Most popular name:", most_popular)
    
def get_text(fname):
    with open(fname) as f: 
        text = f.read()
    return text

def get_words(text):
    word_pattern = "\w+"
    words = re.findall(word_pattern, text)
    return words

def pretty_print_tuple(header, tuple_lst):
    print(header, end =" ")
    for item,count in tuple_lst:
        print (item)
