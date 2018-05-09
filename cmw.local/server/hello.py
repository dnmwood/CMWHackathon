import sys
print(sys.version)
from flask import Flask, abort, request
from flask_cors import CORS
import json
import csv
import gensim
import sklearn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)
CORS(app)


model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

with open('./bands.csv', 'r') as f:
 reader = csv.reader(f)
 csv_bands = list(reader)

data = []

for row in csv_bands:
 vec = []
 for w in row[1].split(" "):
   if w not in model.vocab:
     continue
   vec.append(model.get_vector(w))
 if not vec:
   continue
 row.append(vec)
 row.append(np.average(vec,axis=0))
 data.append(row)

embed = []
genres = []

for row in data:
 for genre in row[2].split(','):
   embed.append(row[-1])
   genres.append(genre)

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(embed, genres)

def ave_word_embed(name):
 vec = []
 for w in name.split(" "):
   if w not in model.vocab:
     continue
   vec.append(model.get_vector(w))
 ave = np.average(vec,axis=0)
 return [ave]

def softmax(x):
   """Compute softmax values for each sets of scores in x."""
   e_x = np.exp(x - np.max(x))
   return e_x / e_x.sum(axis=0)

def top_n(name,n=4):
 probs = neigh.kneighbors(ave_word_embed(name),n)
 predicted_genres = []
 for i in probs[1][0]:
   predicted_genres.append(genres[i])
 return predicted_genres + list(softmax(-1*probs[0][0]))


@app.route("/init", methods=['POST'])
def init():
 # do initialization stuff
 print("I am initializing the server!")

 return "Initialized"

@app.route("/percentage", methods=['GET'])
def percentage():
 # grab the percentages and return them as json
 # with json.dumps
 print(request.args['name'])
 result = top_n(request.args['name'])
 print(result)
 return str(result)
