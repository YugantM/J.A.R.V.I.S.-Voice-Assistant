
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk

jarvis = ChatBot("JARVIS")

jarvis.set_trainer(ListTrainer)

'''
jarvis.train([
    "Hi there!",
    "Hello",
    "Ola",
    "Hi what's up !",
    "Howdy"
])'''
identity = ["who are you","my name is jarvis,i am here to help you","what is your name","jarvis"]
#jarvis.train(identity)

response = jarvis.get_response("what is you name")

string = "open my computer"
print(string.find("open"))
text = nltk.word_tokenize(string)
print(nltk.pos_tag(text))
print(response)

