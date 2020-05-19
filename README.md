# Islamic-chatbot
Chatbot using NLTK & Keras Deep Learning

## About the Islamic chatbot Project
In this Python project with source code, I built a chatbot using deep learning techniques. The chatbot will be trained on the dataset which contains categories (intents), pattern and responses and use a special recurrent neural network (LSTM) to classify which category the user’s message belongs to and then we will give a random response from the list of responses.

### The Dataset
The dataset we will be using is ‘intents.json’. This is a JSON file that contains the patterns we need to find and the responses we want to return to the user. 

The dataset contains 99 documents and 67 classes collecting from theses websites. 
* [Alsunna](https://alsunna.org/115-questions-answered.html#gsc.tab=0)
* [ING](https://ing.org/top-100-frequently-asked-questions-about-muslims-and-their-faith/)

### Prerequisites
In dependencies file, You can see all libraries that need to be install also you need to upload dataset if you will use google colab.


### output generated files
During runing the project, you will see these files is generated

* Words.pkl – This is a pickle file in which we store the words Python object that contains a list of our vocabulary.
* Classes.pkl – The classes pickle file contains the list of categories.
* Chatbot_model.h5 – This is the trained model that contains information about the model and has weights of the neurons.


## How to run Islamic chatbot?
You have the ability to run it online using google colab or run it offline. 
![](Islamic-chatbot/Islamic%20chatbot.png)

**online:**
Open Islamic chatbot file using google colab and upload dataset in root folder

**offline:**
Run theses files by order and download dataset
1. dependencies.py
2. process_data.py
3. training.py
4. sequential model.py
5. predict the response.py
6. Run Islamic chatbot.py

### References
* [Python Chatbot](https://data-flair.training/blogs/python-chatbot-project/)

