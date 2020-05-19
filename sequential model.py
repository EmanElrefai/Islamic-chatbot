#building sequential model with 3 layers 

model=Sequential()
#first layer with 128 neurons
model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
#second layer with 64 neurons
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
#output layer
model.add(Dense(len(train_y[0]),activation='softmax'))

# stochastic gradient decsent
sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
#compiling model
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

#fitting model
hist=model.fit(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose=1,validation_split=0.2)
#saving model
model.save('chatbot_model.h5',hist)

print('model created')