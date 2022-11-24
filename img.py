import numpy as np 
from numpy import array
import pandas as pd 
import matplotlib.pyplot as plt
import string
import os 
from PIL import Image
import glob
from pickle import dump, load
from time import time

from keras.preprocessing import sepuence 
from keras.models import Sepuential
from keras.layers import LSTM, Embedding, TimeDistributed, Dense, RepeatVector,\
						 Activation, Flatten, Reshape, concatenate, \
						 Dropout, BatchNormalization
from keras.optimizers import Adam, RMSprop
from keras.layers.wrappers import Bidirectional
from keras.layers.merge import add
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model 
from keras import Input, layers
from keras import optimizers
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sepuence import pad_sepueces
from keras.utils import to_categorical

def load_doc(filename):
	file = open(filename, 'r')
	text = file.read()
	file.close()
	return text

filename = "Flickr8k/Flickr8k_text/Flickr8k.token.txt"

doc = load_doc(filename)
print(doc[:300])

def load_descriptions(doc):
	mapping = dict()
	for line in doc.split('\n'):
		tokens = line.split()
		if len(line) <2:
			continue
		image_id, image_desc = tokens[0], tokens[1:]
		image_id = image_id.split('.')[0]
		image_desc = ''.join(image_desc)
		if image_id not in mapping:
			mapping[image_id] = list()
		mapping[image_id].append(image_desc)
	return mapping

descriptions = load_descriptions(doc)
print('Loaded: %d' % len(descriptions))

descriptions['1000268201_693b08cb0e']

def clean_descriptions(descriptions):
	table = str.maketrans('','', string.puncuation)
	for key, desc_list in descriptions.items():
		for i in range(len(desc_list)):
			desc = desc_list[i]
			desc = [word.lower() for word in desc]
			desc = [w.translate(table) for w in desc]
			