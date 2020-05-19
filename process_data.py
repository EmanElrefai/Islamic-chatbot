words=[]
documents=[]
classes=[]
ignore_words=['?','!','.','“', '”','(', ')', ',','’']

data_file = open('intents.json',)
intents=json.load(data_file)

nltk.download('wordnet')

for intent in intents['intents']:
  for pattern in intent['patterns']:
    w=nltk.word_tokenize(pattern)
    words.extend(w)

    documents.append((w,intent['tag']))
    # add to our classes list
    if intent['tag'] not in classes:
      classes.append(intent['tag'])

#lemizer and lower each word and remove duplicates
words=[lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words=sorted(list(set(words)))

#sort classes
classes=sorted(list(set(classes)))

#decuments= pattern , intents
print(len(documents),"documents")
#classes= intents
print(len(classes),"classes",classes)
#words = each words , vocabulary
print(len(words),"unique lemmatized words",words)

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

