# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:54:00 2021

@author: pc
"""

import tr
import nltk,pprint,sys,os
from nltk.corpus import stopwords
from nltk import word_tokenize,bigrams,trigrams
from timeit import default_timer as timer

path = '0'

def file_read(path):
    try:
        f = open(path,encoding='utf-8')
        return f.read()
    except FileNotFoundError:
        print("File doesn't exist!!")
    
def prepare_words(raw):
    stop_words = set(stopwords.words('turkish'))
    tokens = word_tokenize(raw)
    return [tr.lower(w) for w in tokens if w.isalpha() and w not in stop_words]

def print_results(unidist,bidist,tridist):
    pp = pprint.PrettyPrinter()
   
    print('------ 1-GRAM Results -------')
    pp.pprint(unidist.most_common(100))
    
    print('\n\n------ 2-GRAM Results -------')
    pp.pprint(bidist.most_common(100))
    
    print('\n\n------ 3-GRAM Results -------')
    pp.pprint(tridist.most_common(100))
    

def n_gram_without_probability():
    raw = file_read(path)
    
    uni_words = prepare_words(raw)  
    unidist = nltk.FreqDist(uni_words)
    
    bi_words = list(bigrams(uni_words))
    bidist = nltk.FreqDist(bi_words)
    
    tri_words = list(trigrams(uni_words))
    tridist = nltk.FreqDist(tri_words)
    
    print_results(unidist,bidist,tridist)
    
def n_gram_with_probability():
    raw = file_read(path)
    
    uni_words = prepare_words(raw)
    vocab = set(uni_words)
    unidist = nltk.FreqDist(uni_words)
    
    for i in vocab:
        unidist[i] = unidist[i]/len(uni_words)
        
    bi_vocab = set(list(bigrams(uni_words)))
    bidist = nltk.FreqDist()
    
    for j in bi_vocab:
        bidist[j] = (unidist[list(j)[0]]) * (unidist[list(j)[1]])
        
    tri_vocab = set(list(trigrams(uni_words)))
    tridist = nltk.FreqDist()
    
    for k in tri_vocab:
        tridist[k] = (unidist[list(k)[0]]) * (unidist[list(k)[1]]) * (unidist[list(k)[2]])

    print_results(unidist,bidist,tridist)
    
if __name__ == "__main__":
    novels = ["BİLİM İŞ BAŞINDA.txt","BOZKIRDA.txt","DEĞİŞİM.txt","DENEMELER.txt","UNUTULMUŞ DİYARLAR.txt"]
    states = {'Menu':0, 'Selection':1, 'Result':2}
    state = 0
    first = 0
    second = 0
    clear = lambda: os.system('cls')
    while 1:
        clear()
        if state == states['Menu']:
            first = 0
            print("------ NLP N-GRAM CALCULATOR ------")
            print("\n")
            print("1 - Bilim İş Başında")
            print("2 - Bozkırda")
            print("3 - Değişim")
            print("4 - Denemeler")
            print("5 - Unutulmuş Diyarlar")
            first = input("\n\n\n Please Select a Novel : ")
            
            if first == 'exit': sys.exit()
            
            elif '12345'.__contains__(first) and first != '':
                state = states['Selection']
        
        elif state == states['Selection']:
            second = 0
            print("------ NLP N-GRAM CALCULATOR ------")
            print("\n")
            print("1 - Calculate Top 100 N-Gram Without Probability")
            print("2 - Calculate Top 100 N-Gram With Probability")
            
            second = input("\n\n\n Please Select N-Gram Method : ")
            
            if second == 'exit': sys.exit()
            
            elif second == '1' or second == '2':
                state = states['Result']
        
        elif state == states['Result']:
            path = novels[int(first)-1]
            if second == '1':
                start = timer()
                n_gram_without_probability()
                end = timer()
                print("\n\nElapsed Time for Top 100 N-Gram Without Probability :",(end-start)*1000,"Milliseconds")
            else:
                start = timer()
                n_gram_with_probability()
                end = timer()
                print("\n\nElapsed Time for Top 100 N-Gram With Probability :",(end-start)*1000,"Milliseconds")
            
            wait = input()
            state = states['Menu']
            
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
