def clean_up_sentence(sentence):
  #toknize sentence
  sentence_words=nltk.word_tokenize(sentence)
  #lemmtaized and lower each word
  sentence_words=[lemmatizer.lemmatize(word.lower()) for word in sentence_words]

  return sentence_words

def bow(sentence,words,show_details=False):
  #cleaning up sentence
  sentence_words=clean_up_sentence(sentence)

  bag=[0]*len(words)

  for s in sentence_words:
    for i,w in enumerate(words):
      if w==s:
        # bag equal one if current word is in the vocabulary position
        bag[i]=1

        if show_details==True:
          print('Found in %s',w)

  return np.array(bag)

def predict_class(sentence,model):
  #filter prediction that below threshold
  p=bow(sentence,words,show_details=False)
  res=model.predict(np.array([p]))[0]

  ERROR_THRESHOLD=0.25

  results=[[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
  
  #sort by strong probability
  results.sort(key=lambda x:x[1],reverse=True)
  
  return_list=[]
  for r in results:
      return_list.append({"intent":classes[r[0]],"probability":str(r[1])})
  
  
  return return_list

