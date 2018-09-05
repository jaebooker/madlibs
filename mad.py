import random
from random import shuffle
# from tts_watson.TtsWatson import TtsWatson
#
# ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice')
# ttsWatson.play("Good Morning, Starshine! The earth says hello!")
# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")
import pyttsx
engine = pyttsx.init()
choice = raw_input("Do you want to randomize your answers? (y/n) ")
word1 = raw_input("Enter a name: ")
word2 = raw_input("Enter a verb: ")
word3 = raw_input("Enter another verb: ")
word4 = raw_input("Enter a noun: ")
word5 = raw_input("Enter an ajective: ")
word6 = raw_input("Enter a verb: ")
word7 = raw_input("Enter a noun: ")
word8 = raw_input("Enter a verb: ")
word9 = raw_input("Enter a verb: ")
word10 = raw_input("Enter an ajective: ")
#story = word1 + " walked into MakeSchool, hoping to " + word2 + ", or at least " + word3 + ". Carrying only a " + word4 + ". Taking off their shoes, the " + word5 + " expression on the students' faces meant they were certainly going to " + word6 + ". However, the " + word7 + " had no interest to " + word8 + ", instead choosing to " + word9 + " " + word10
#print(story)
words = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10]
answer = choice.lower()
name = word1
nouns = [word4, word7]
ajectives = [word5, word10]
verbs = [word2, word3, word6, word8, word9]
sentences = [" walked into MakeSchool, hoping to ", ", or at least ", ", carrying only a ", ". Taking off their shoes, the ", " expressions on the students' faces meant they were certainly going to ", ". However, the ", " had no interest to ", ", instead choosing to ", " in an action most "]
sentences2 = [" was sick of having to ", " all the time. Secretly, hoping to ", " instead. To everyone's great shock and horror, a ", " could be seen moving silently across the floor, looking as ", " as ever, probably planning a deceptive scheme to ", ". The ", " was even worse, wishing to ", " like all the others. Or else it would ", ", in a fate most "]
sentences3 = [" and the others had a trick up their sleeves. They were planning to ", " and then ", ", using only a ", ": a most ", " plot indeed. Very few would be so willing to ", " a ", ". Now, either they would ", " or else ", ", in a manner most "]
def tellStory():
    for i in range(0,10):
        if i != 9:
            print(words[i] + sentences[i])
        else:
            print(words[i])
def randomStory():
    shuffle(nouns)
    shuffle(ajectives)
    shuffle(verbs)
    random_sentence = random.randrange(0,3)
    if random_sentence == 0:
        new_sentence = sentences
    elif random_sentence == 1:
        new_sentence = sentences2
    else:
        new_sentence = sentences3
    #new_sentence = sentences
    new_story = name + new_sentence[0]
    verb_count = 0
    noun_count = 0
    for i in range(1,10):
        if i == 3 or i == 6:
            new_story += nouns[noun_count]
            new_story += new_sentence[i]
            noun_count += 1
        elif i == 4:
            new_story += ajectives[0]
            new_story += new_sentence[i]
        elif i == 9:
            new_story += ajectives[1]
        else:
            new_story += verbs[verb_count]
            new_story += new_sentence[i]
            verb_count += 1
    print(new_story)
    engine.say(new_story)
    engine.runAndWait()


def answer_choice():
    if answer == 'y':
        randomStory()
    else:
        tellStory()
answer_choice()
def test():
    print("Running test")
    word1 = "Jerremy"
    word2 = "run"
    word3 = "stride"
    word4 = "horse"
    word5 = "boyish"
    word6 = "live"
    word7 = "turtle"
    word8 = "fly"
    word9 = "die"
    word10 = "gracefully"
    print(story)
#test()
