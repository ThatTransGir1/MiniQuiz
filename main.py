import pyfiglet
import time
import datetime
import json
import os
import sys
from requests import get as rget

res = rget("https://thegamershollow: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@raw.githubusercontent.com/thegamershollow/miniquizquestions/main/questions.json")

points = 0
qnum = 1
endq = "False"
jsonpath = "questions.json"
f = open(jsonpath)
data = json.load(f)
q1 = data[0]
q2 = data[1]
q3 = data[2]
q4 = data[3]
q5 = data[4]
q6 = data[5]
q7 = data[6]
q8 = data[7]
q9 = data[8]
q10 = data[9]
q11 = data[10]

def countdown(s):
  global endq
  total_seconds = s
  while total_seconds > 0:
    timer = datetime.timedelta(seconds = total_seconds)
    print(timer, end="\r")
    time.sleep(1)
    total_seconds -= 1
  sys.exit("You ran out of time, better luck next time :D")

def jprint(var):
  global qnum
  print("Question: " + str(qnum) +"\n" + var["question"]+"\nA. "+var["A"]+"\nB. "+var["B"]+"\nC. "+var["C"]+"\nD. "+var["D"])

def check(var):
  return var["answer"]

def question(qn,pval,qns,pnts):
  global points
  global qnum
  global data
  jprint(qn)
  i = input("Answer: ")
  c = check(qn)
  i = i.upper()
  if i == c:
    print("Correct, the answer to " + str(qnum) + " is " + c + ". You get " + str(pval) + " points.")
    points = pnts + pval
  else:
    print("Wrong, the correct answer for question " + str(qnum) + " is " + c)
  qnum = qns + 1
  time.sleep(2)
  os.system("clear")
def questions():
  question(q1,pval=4,qns=qnum,pnts=points)
  question(q2, pval=2, qns=qnum, pnts=points)
  question(q3, pval=2, qns=qnum, pnts=points)
  question(q4, pval=2, qns=qnum, pnts=points)
  question(q5, pval=4, qns=qnum, pnts=points)
  question(q6, pval=2, qns=qnum, pnts=points)
  question(q7, pval=4, qns=qnum, pnts=points)
  question(q8, pval=2, qns=qnum, pnts=points)
  question(q9, pval=2, qns=qnum, pnts=points)
  question(q10, pval=2, qns=qnum, pnts=points)
  question(q11, pval=4, qns=qnum, pnts=points)
def start():
  os.system("clear")
  print(" __      __       .__                               \n/  \    /  \ ____ |  |   ____  ____   _____   ____  \n\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ \n \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ \n  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >\n       \/       \/          \/            \/     \/ ")
  print("This is a quiz on Pseudocode and Flowcharts.\n\n")
  print("If you use the timer you will have 3 minutes to complete the quiz.")
  var = input("Would you like to use a timer [y/n]: ")
  i = input("Press enter to start the quiz:")
  if var.lower() == "y":
    countdown(180)
  os.system("clear")
  print("The quiz has started\n\n")
start()
questions()
print("You have finished the quiz your score is: " + points + "/30.")
#f.close