# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:33:40 2020

@author: Faheem
"""
import re
import collections
import pandas as pd

d = dict()
d1=dict() 
l=list()

f1= open('Gull.txt',encoding="utf8").read()
new_str = re.sub('\W+',' ', f1)
new_str = new_str.lower()
open('f3.txt', 'w').write(new_str)
f2=open('Tale.txt',encoding="utf8").read()
new_str1 = re.sub('\W+',' ', f2)
new_str1 = new_str1.lower()
open("f4.txt", "w+", encoding="utf8").write(new_str1)
f3=open('Gull.txt',encoding="utf8")
f4=open('Tale.txt',encoding="utf8")
for word in set(f3.read().split()) & set(f4.read().split()):
    print(word)
    k = 0 
    with open('f3.txt', 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if(i==word):
                    k=k+1
    d[word]=k
    
    k1 = 0 
    with open('f4.txt', 'r') as f1:
        for line1 in f1:
            words1 = line1.split()
            for i in words1:
                if(i==word):
                    k1=k1+1
    d1[word]=k1

n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(d)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)# Close the file
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')

n_print1 = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print1))
word_counter = collections.Counter(d1)
for word, count in word_counter.most_common(n_print1):
    print(word, ": ", count)# Close the file
# Draw a bar chart
lst1 = word_counter.most_common(n_print1)
df = pd.DataFrame(lst1, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')