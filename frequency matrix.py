# -*- coding: utf-8 -*-
"""DL_lab4_E18CSE037.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BvYcxVSX34-mqfCtEMcW90g1btZXGalk
"""

import pandas as pd
import numpy as np

data=pd.read_csv("/content/quotes.txt",header=None,error_bad_lines=False)

data

data.shape

arr=data[0]

arr=np.array(arr)

import nltk
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

!pip install -q wordcloud
import wordcloud

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 

import pandas as pd
import matplotlib.pyplot as plt
import io
import unicodedata
import numpy as np
import re
import string

"""**Tokenize**"""

from nltk.tokenize import sent_tokenize,word_tokenize
new_arr=[]
lst=[]
for i in arr:
  i=i.lower()
  i=re.sub('[^a-zA-Z]',' ',i)
  i=word_tokenize(i)
  lst.append(i)

lst=np.array(lst)

"""**Stop words removal and Stemming**"""

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
ps=PorterStemmer()
stop_words=set(stopwords.words('english'))
fin=[]
for w in lst:
  new_arr=[]
  for i in w:
    if i not in stop_words:
      i=lemmatizer.lemmatize(i)
      new_arr.append(i)
    fin.append(new_arr)

print(stopwords.words('english'))

fin=np.array(fin)

fin

"""**Frequency Matrix**"""

unique=[]
for i in fin:
  for j in i:
    if j not in unique:
      unique.append(j)

df=pd.DataFrame(data=[[0]*22]*40,columns=unique)

df=df.values

df

"""**Defining X and Y**"""

X=np.array(df)
y=pd.read_csv("/content/quotes_y.txt",header=None,error_bad_lines=False)
y=np.array(y)

"""0=Demotivational
1=Motivational
"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

"""**Model**"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.layers import Dense

model=keras.Sequential()

model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X_train,y_train,epochs=200,batch_size=32,verbose=None)

"""**Evaluation**"""

_,accuracy=model.evaluate(X_train,y_train)
print("Accuracy: %2f" % (accuracy*100))

def general(node,X_train,y_train):
  model = keras.Sequential()
  model.add(Dense(node, activation='relu'))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  start = time.time()
  model.fit(X_train, y_train, epochs=500,verbose = None,batch_size=10)
      # sleeping for 1 sec to get 10 sec runtime
  time.sleep(1)

  # end time
  end = time.time()
  _, train_acc = model.evaluate(X_train, y_train)
  _, test_acc = model.evaluate(X_test,y_test)

  total = end-start
  return train_acc, test_acc, total

import time
train = []
test = []
total_time = []
label = [8, 16, 32,64, 128, 256, 512, 1028]
for i in label:
  train_acc, test_acc, total = general(i,X_train, y_train)
  train.append(train_acc)
  test.append(test_acc)
  total_time.append(total)

"""**Analysis**"""

import matplotlib.pyplot as plt 
# creating the bar plot 
plt.bar(label, train, width = 10) 

plt.xlabel("No. of Nodes") 
plt.ylabel("Training Accuracy") 
plt.title("Training Acc v/s No. of Nodes") 
plt.show() 

plt.bar(label, test, width = 10 ) 
  
plt.xlabel("No. of Nodes") 
plt.ylabel("Testing Accuracy") 
plt.title("Testing Acc v/s No. of Nodes") 
plt.show() 

plt.bar(label, total_time, width = 10 ) 
  
plt.xlabel("No. of Nodes") 
plt.ylabel("Running Time") 
plt.title("Running Time v/s No. of Nodes") 
plt.show()

"""**Analysis**"""

def model_lay(n,X_train,y_train):
  model = keras.Sequential()
  if(n==2):
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

  elif(n==3):
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
  elif(n==4):
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
  elif(n==5):
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
  
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  start = time.time()
  model.fit(X_train, y_train, epochs=500,verbose = None,batch_size=1)
      # sleeping for 1 sec to get 10 sec runtime
  time.sleep(1)

  # end time
  end = time.time()
  _, train_acc = model.evaluate(X_train, y_train)
  _, test_acc = model.evaluate(X_test,y_test)

  total = end-start
  return train_acc, test_acc, total

import time
train = []
test = []
total_time = []
label = [2,3,4,5]
for i in label:
  train_acc, test_acc, total = model_lay(i,X_train, y_train)
  train.append(train_acc)
  test.append(test_acc)
  total_time.append(total)

import matplotlib.pyplot as plt 
# creating the bar plot 
plt.bar(label, train) 

plt.xlabel("No. of Layers") 
plt.ylabel("Training Accuracy") 
plt.title("Training Acc v/s No. of Layers") 
plt.show() 

plt.bar(label, test ) 
  
plt.xlabel("No. of Layers") 
plt.ylabel("Testing Accuracy") 
plt.title("Testing Acc v/s No. of Layers") 
plt.show() 

plt.bar(label, total_time ) 
  
plt.xlabel("No. of Layers") 
plt.ylabel("Running Time") 
plt.title("Running Time v/s No. of Layers") 
plt.show()