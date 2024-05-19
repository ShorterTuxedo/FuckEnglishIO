import keyboard
import pyttsx3
import random
import playsound
import time

def getXinRangeVars(X, rangeVars):
    myThresholds=list(rangeVars.keys())
    myInd=None
    for i in range(len(myThresholds)):
        if X<int(myThresholds[i]):
            break
        myInd=i
    isLast = (myInd == len(myThresholds) - 1)
    return (isLast, myInd,myThresholds[myInd], rangeVars[myThresholds[myInd]], myThresholds)

###consts###
reminderMode = True
candidateName = "Joe Bloggs"
PPronoun = "His"
cCode = "job123"
#the location of the microsoft voice, you need to install them in your settings for it to work (just google install spanish voice package)
iovoice = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"]
#determines the speed of the voice, higher is faster (wpm)
defaultVoiceRate=125
newVoiceRate = defaultVoiceRate
try:
    newVoiceRate=int(input("Voice rate?(default is 125)"))
except:
    newVoiceRate=defaultVoiceRate
#determines the number of questions asked before the program moves onto a new batch of qs
batchSize = int(input("How many questions to ask in this IO?"))
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
    batch=random.sample(questions, batchSize)
    ct = 0
    for text in batch:
        print(text)
        engine.say(text)
        engine.runAndWait()
        print("When you have completed your answer, hold \"S\" on your keyboard for 2 seconds.")
        pastTime = time.time()
        finishedQuestion = False
        while ct<300 and not finishedQuestion:
                if keyboard.is_pressed('s'):
                    finishedQuestion = True
                time.sleep(1)
                ct += 1
        playsound.playsound("CHIMES.wav")
        print("Question complete.")
        print("Answering time: ", time.time()-pastTime, "s")
        time.sleep(1)
        if not finishedQuestion:
               print("Thank you. However, you must now halt your answer, as our time has lapsed.")
               engine.say("Thank you. However, you must now halt your answer, as our time has lapsed.")
               engine.runAndWait()
               break
        #time in seconds it has taken you to answer, because why not
    print("The discussion section is now complete.")
    engine.say("The discussion section is now complete.")
    engine.runAndWait()

startingYap=f"The candidate's name is {candidateName}. {PPronoun} candidate code is {cCode}. {candidateName}, you may now begin."
print(startingYap)
engine.say(startingYap)
engine.runAndWait()
print("When you have finished, hold \"S\" on your keyboard for 2 seconds.")
finished=False
ct=0
if reminderMode:
    print("Reminder mode is on. It gives you as to when to start your sections of the IO.")
while ct<630 and not finished:
    print(ct, "seconds have elapsed.")
    if reminderMode:
        if ct == 0:
            print("We are at the 0 second mark. Please begin your introduction.")
            engine.say("We are at the 0 second mark. Please begin your introduction.")
            engine.runAndWait()
        elif ct == 90:
            print("We are currently at the 1 min 30 s mark. Please begin describing your extract in text A.")
            engine.say("We are currently at the 1 minute 30 second mark. Please begin describing your extract in text A.")
            engine.runAndWait()
        elif ct == 210:
            print("We are currently at the 3 min 30 s mark. Please begin describing the wider body of work of text A.")
            engine.say("We are currently at the 3 minute 30 second mark. Please begin describing the wider body of work of text A.")
            engine.runAndWait()
        elif ct == 300:
            print("We are currently at the 5 min mark. Please begin describing your extract in text B.")
            engine.say("We are currently at the 5 minute mark. Please begin describing your extract in text B.")
            engine.runAndWait()
        elif ct == 420:
            print("We are currently at the 7 min mark. Please begin describing the wider body of work of text B.")
            engine.say("We are currently at the 7 minute mark. Please begin describing the wider body of work of text B.")
            engine.runAndWait()
        elif ct == 540:
            print("We are currently at the 9 min mark. Please begin your conclusion.")
            engine.say("We are currently at the 9 minute mark. Please begin your conclusion.")
            engine.runAndWait()
    if keyboard.is_pressed('s') and (ct<630):
        if (ct<570):
            print("You are not permitted to terminate your analysis.")
        else:
            finished = True
    time.sleep(1)
    ct += 1
if not finished:
   print("Thank you. However, you must now stop your analysis, as our time has lapsed.")
   engine.say("Thank you. However, you must now stop your analysis, as our time has lapsed.")
   engine.runAndWait()
else:
   print(f"Your analysis took {ct} seconds.")
print("Thank you. We will now begin the discussion.")
engine.say("Thank you. We will now begin the discussion.")
engine.runAndWait()
batch()
print("Thank you. We have now completed the individual oral assessment.")
engine.say("Thank you. We have now completed the individual oral assessment.")
engine.runAndWait()

cAm={"0":"The work does not reach a standard described by the descriptors below.", "1":"There is little knowledge and understanding of the extracts and the works/texts in relation to the global issue. References to the extracts and to the works/texts are infrequent or are rarely appropriate.","3":"There is some knowledge and understanding of the extracts and the works/texts in relation to the global issue. References to the extracts and to the works/texts are at times appropriate","5":"There is satisfactory knowledge and understanding of the extracts and the works/texts and an interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are generally relevant and mostly support the candidate’s ideas.","7":"There is good knowledge and understanding of the extracts and the works/texts and a sustained interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are relevant and support the candidate’s ideas.","9":"There is excellent knowledge and understanding of the extracts and of the works/texts and a persuasive interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are well chosen and effectively support the candidate’s ideas."}
cBm={"0":"The work does not reach a standard described by the descriptors below.","1":"There is little knowledge and understanding of the extracts and the works/texts in relation to the global issue. References to the extracts and to the works/texts are infrequent or are rarely appropriate.","3":"There is some knowledge and understanding of the extracts and the works/texts in relation to the global issue. References to the extracts and to the works/texts are at times appropriate.","5":"There is satisfactory knowledge and understanding of the extracts and the works/texts and an interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are generally relevant and mostly support the candidate’s ideas.","7":"There is good knowledge and understanding of the extracts and the works/texts and a sustained interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are relevant and support the candidate’s ideas.","9":"There is excellent knowledge and understanding of the extracts and of the works/texts and a persuasive interpretation of their implications in relation to the global issue. References to the extracts and to the works/texts are well chosen and effectively support the candidate’s ideas."}
cCm={"0":"The work does not reach a standard described by the descriptors below.","1":"The oral rarely focuses on the task. There are few connections between ideas.", "3":"The oral only sometimes focuses on the task, and treatment of the extracts, and of the works/texts may be unbalanced. There are some connections between ideas, but these are not always coherent.", "5": "The oral maintains a focus on the task, despite some lapses; treatment of the extracts and works/texts is mostly balanced. The development of ideas is mostly logical; ideas are generally connected in a cohesive manner.", "7": "The oral maintains a mostly clear and sustained focus on the task; treatment of the extracts and works/texts is balanced. The development of ideas is logical; ideas are cohesively connected in an effective manner.","9":"The oral maintains a clear and sustained focus on the task; treatment of the extracts and works/texts is well balanced. The development of ideas is logical and convincing; ideas are connected in a cogent manner."}
cDm={"0":"The work does not reach a standard described by the descriptors below.","1":"The language is rarely clear or accurate; errors often hinder communication. Vocabulary and syntax are imprecise and frequently inaccurate. Elements of style (for example, register, tone and rhetorical devices) are inappropriate to the task and detract from the oral.","3":"The language is generally clear; errors sometimes hinder communication. Vocabulary and syntax are often imprecise with inaccuracies. Elements of style (for example, register, tone and rhetorical devices) are often inappropriate to the task and detract from the oral.", "5":"The language is clear; errors do not hinder communication. Vocabulary and syntax are appropriate to the task but simple and repetitive. Elements of style (for example, register, tone and rhetorical devices) are appropriate to the task and neither enhance nor detract from the oral.", "7":"The language is clear and accurate; occasional errors do not hinder communication. Vocabulary and syntax are appropriate and varied. Elements of style (for example, register, tone and rhetorical devices) are appropriate to the task and somewhat enhance the oral.","9":"The language is clear, accurate and varied; occasional errors do not hinder communication. Vocabulary and syntax are varied and create effect. Elements of style (for example, register, tone and rhetorical devices) are appropriate to the task and enhance the oral."}
gBound={"0":"1","7":"2","13":"3","19":"4","24":"5","29":"6","34":"7"}
print("\n\n\n\n\n\nThank you. You may give marks on your own IO or ask a friend/teacher to help.")
print("Marking Guide for Criterion A: ")
for x in cAm.keys():
    print((x if x == "0" else (str(x) + " - " + str(int(x) + 1))), "Marks")
    print(cAm[x])
critA=None
while critA==None:
    try:
        critA=int(input("Marks on criterion A?"))
        critA = critA if (critA>=0 and critA<=10) else None
    except Exception:
        critA=None
print("\n\n\n\n\n\nMarking Guide for Criterion B: ")
for x in cBm.keys():
    print((x if x == "0" else (str(x) + " - " + str(int(x) + 1))), "Marks")
    print(cBm[x])
critB=None
while critB==None:
    try:
        critB=int(input("Marks on criterion B?"))
        critB = critB if (critB>=0 and critB<=10) else None
    except Exception:
        critB=None
print("\n\n\n\n\n\nMarking Guide for Criterion C: ")
for x in cCm.keys():
    print((x if x == "0" else (str(x) + " - " + str(int(x) + 1))), "Marks")
    print(cCm[x])
critC=None
while critC==None:
    try:
        critC=int(input("Marks on criterion C?"))
        critC = critC if (critC>=0 and critC<=10) else None
    except Exception:
        critC=None
print("\n\n\n\n\n\nMarking Guide for Criterion D: ")
for x in cDm.keys():
    print((x if x == "0" else (str(x) + " - " + str(int(x) + 1))), "Marks")
    print(cDm[x])
critD=None
while critD==None:
    try:
        critD=int(input("Marks on criterion D?"))
        critD= critD if (critD>=0 and critD<=10) else None
    except Exception:
        critD=None
print("\n\n\n\n\n\nMark Breakdown:")
print("Criterion A: ", critA, "/ 10")
print(getXinRangeVars(critA, cAm)[3])
print("Criterion B: ", critB, "/ 10")
print(getXinRangeVars(critB, cBm)[3])
print("Criterion C: ", critC, "/ 10")
print(getXinRangeVars(critC, cCm)[3])
print("Criterion D: ", critD, "/ 10")
print(getXinRangeVars(critD, cDm)[3])
total=critA+critB+critC+critD
print("\n\n\nTotal Mark: ", total, " / 40\n\n\n")
gHolds=list(gBound.keys())
for i in range(len(gHolds)):
    print(gHolds[i], " - ", ("40" if i == len(gHolds) - 1 else str(int(gHolds[i+1])-1)), "marks for a", gBound[gHolds[i]])
myGrade = getXinRangeVars(total, gBound)
myUpperBound = (40 if myGrade[0] else (int(myGrade[4][myGrade[1]+1])-1))
myLowerBound = int(myGrade[2])
gradeLMH = (total-myLowerBound)/(myUpperBound - myLowerBound)
lowMidOrHighGrade = ("Low" if gradeLMH <= (1/3) else ("Mid" if gradeLMH <= (2/3) else "High"))
print("\n\n\n",lowMidOrHighGrade,myGrade[3])
