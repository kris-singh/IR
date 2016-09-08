import nltk
import pandas as pd
import sklearn
import numpy as np
import os
import re
import datefinder 
list_files = os.listdir('./Text_files/')
corpus = []
for i in list_files:
	corpus.append(open('./Text_files/'+i).read())
corpus = "".join(corpus)
#corpus_words  = nltk.word_tokenize(corpus.decode('utf-8'))
#print corpus
#create corpus1 
regex_email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#regex_date = ''
#only finds web links and external not internal
regex_url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(regex_url,corpus)
email = re.findall(regex_email,corpus)
#date = re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', corpus)
matches = list(datefinder.find_dates(corpus))
if len(matches) > 0 :
	date = matches[0]
	print date
else:
	print "No dates Found"

#stop = set(nltk.corpus.stopwords.words('/home/kris/Desktop/IR/ass2/stop_words.txt'))
#corpus_words = [i for i in corpus_words if i not in stop]


