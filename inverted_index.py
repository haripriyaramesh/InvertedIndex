import nltk
from nltk.corpus import stopwords
import os
import glob
def create_index(tokens):
    inverted_index = {}
    wordCount = {}
    for k, v in tokens.items():
        for word in v.lower().split():
            wordCount[word] = wordCount.get(word,0)+1
            if inverted_index.get(word,False):
                if k not in inverted_index[word]:
                    inverted_index[word].append(k)
            else:
                inverted_index[word] = [k]
    return inverted_index

i=1 #assigns document no
t={} #dictionary for storing documents, with document no. as key and words as value
path='C:/Python27/assignment'
for filename in glob.glob( os.path.join(path,'*.txt')):
    fp= open(filename)
    f= fp.read()
    t[i]=f
    i=i+1

index = create_index(t) #stores inverted index dict
#print index
    
query = raw_input("Enter query")
def removing_stopwords(text):               #Removing Stopwords like "the"
    stopwords = nltk.corpus.stopwords.words('english')
    query = [w for w in text.split() if w.lower() not in stopwords]
    return query

query = removing_stopwords(query)  
query = ' '.join(query)
query = set(w.lower() for w in query.split()) #Normalizing the query
query = ' '.join(query)

tokenised_query = [] 
tokenised_query = nltk.word_tokenize(query) #tokenized query
print "the tokenised query is", tokenised_query
l = [] #list which stores the postings values of the words that matched the query

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

stemmed_query = []
for each in tokenised_query:
    stemmed_query.append(stem(each))

print "The stemmed query is ", stemmed_query
for i in stemmed_query:
    for k in index.keys():
        if stem(k) == i:
            print stem(k), "is found in documents " , index[k]
            l.append(index[k])
leng = len(l)
print "length is", leng #finds out how many words' postings list is chosen 

def common_elements(list1, list2,list3):
    for element in list1:
        if element in list2:
            print '-' * 150
            print "PRESENT IN DOCUMENT NUMBER ",element
            print '*' * 150
            print t[element]

final_docs = []
if leng == 1:
    a = l[0]
    b = []
    c = []
    common_elements(a,b,c)

elif leng == 2:
    a=l[0]
    b=l[1]
    c = []
    common_elements(a,b,c)

elif leng == 3:
    a = l[0]
    b = l[1]
    c = l[2]
    final_docs = common_elements(a,b,c)
    print final_docs
else:
    print "Please enter a shorter query"

