#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

    print(return_evens(num_list))

def make_exclamation(sentence_list):
   
    return [sentence_list + "!" for sentence_list in sentence_list]
    sentence_list = (["Hello", "I'm doing great", "Python is fun"])
    print(make_exclamation(sentence_list))