#create training data
training=[]

#create output  empty array
output_=[0]*len(classes)


#bag of words algorithm
for doc in documents:
    #intialize bag for each word
    bag=[]

    pattern_word=doc[0]

    #lemmatize and lower each word in pattern_word
    pattern_word=[lemmatizer.lemmatize(word.lower()) for word in pattern_word]

    for w in words:
      bag.append(1) if w in pattern_word else bag.append(0)

    #output 
    output_row=list(output_)
    output_row[classes.index(doc[1])]=1
    
    training.append([bag,output_row])

#shuffel features and turn into array
random.shuffle(training)
training=np.array(training)

#train_x is input and train_y is output
train_x=list(training[:,0])
train_y=list(training[:,1])

print('training data created')

