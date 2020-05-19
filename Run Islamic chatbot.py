def getResponse(ints,intents_json):
  tag=ints[0]['intent']
  list_intents=intents_json['intents']

  for i in list_intents:

    if (tag==i['tag']):
      result=random.choice(i['responses'])
      break

  return result


def chatbot_response(msg):
  ints=predict_class(msg,model)
  res=getResponse(ints,intents)

  return res

print(colored("WELCOME TO ISLAMIC CHATBOT", 'red'))
print("")
while(1):
  request=input("")
  response=chatbot_response(request)
  print(colored(response, 'cyan'))
  
  if request=="goodbye"or request== "Bye" or request=="See you later" or request== "Goodbye" or request=="Nice chatting to you, bye" or request=="Till next time":
    break