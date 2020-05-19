import nltk 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download("punkt")
import json
import pickle


import numpy as np
import random
from keras.models import Sequential
from keras.layers import Activation,Dropout,Dense
from keras.optimizers import SGD
from keras.models import load_model

#chatbot gui
from termcolor import colored