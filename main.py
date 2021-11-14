# -*- coding: utf-8 -*-
 
from data_extraction import *

fname = input("Enter file name:")

num_rows(fname)
num_words(fname)
num_unique_words(fname)
avg_and_max_sentence_len(fname)
most_popular_word(fname)
longest_no_k_seq(fname)
people_names(fname)
