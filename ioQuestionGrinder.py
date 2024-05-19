import pyttsx3
import random
import playsound
import time

###consts###
#the location of the microsoft voice, you need to install them in your settings for it to work (just google install spanish voice package)
iovoice = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"]
#determines the speed of the voice, higher is faster (wpm)
defaultVoiceRate=125
newVoiceRate = defaultVoiceRate
try:
    newVoiceRate=int(input("Voice rate?(default is 125)"))
except:
    newVoiceRate=defaultVoiceRate
#determines the number of questions asked before the program moves onto a new batch of qs
countdownmode=input("Countdown mode?").lower()=="true"
batchSize = int(input("Batch size?"))
countdownTime=int(input("Countdown timing?"))
engine = pyttsx3.init()
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', iovoice[0])

#question list, edit the text file and put line breaks between questions to add your own list
f = open("questionList.txt","r",encoding="utf_8_sig")
questions = f.read().split('\n')

#main batch loop
#has a list of x questions which it picks from randomly
#once you say you're confident in it, it will ask it once more then remove it from the list
#batch ends once the list is empty
def batch():
    batch=[questions[random.randint(0,len(questions)-1)] for i in range(batchSize)] #could have multiple of the same q

    confident=[]
    #set to ensure questions aren't added to the text file multiple times
    unconf=set()

    while (len(batch)!=0):
        text=batch[random.randint(0,len(batch)-1)]
        if not countdownmode:
            pastTime=time.time() 
        engine.say(text)
        engine.runAndWait()
        if countdownmode:
            ct=countdownTime
            while ct>0:
                print(ct)
                time.sleep(1)
                ct -= 1
            print("0")
            playsound.playsound("CHIMES.wav")
            print("Time is up.")
        store=input("Were you confident in your answer?(Y/N)\n")
        if store.lower()=='y':
            print(f"You're done! That question was:\n{text}")
            if (text in confident):
                print("You're done with this question! Let's move on.")
                confident.remove(text)
                batch.remove(text)
            else:
                print("You're confident with it. Let's try it again.")
                confident.append(text)
        else:
            print(f"You're done! That question was:\n{text}")
            #any question that is not immediately answered with confidence is added to unconf
            #written to text file at the end of a batch
            unconf.add(text)
            print("Oops! You feel quite unconfident about it. Let's do this again.")
        #time in seconds it has taken you to answer, because why not
        if not countdownmode:
            print(time.time()-pastTime)
        time.sleep(1)
    
    print("Batch Complete")
    
    f=open("Uncertain_Questions.txt",'a',encoding="utf-8")
    for q in unconf:
        f.write("%s\n"%(q.strip()))
    f.close()

    
loopNumber = int(input("How many batches would you like to do? (-1 for endless)\n"))

if (loopNumber == -1):
    while True:
        batch()
else:
    for i in range(loopNumber):
        batch()

print("All batches completed.")

