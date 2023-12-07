import pyfiglet
import time
import datetime
import json
def countdown(s):
  total_seconds = s
  while total_seconds > 0:
    timer = datetime.timedelta(seconds = total_seconds)
    print(timer, end="\r")
    time.sleep(1)
    total_seconds -= 1
    print("Time is up")
points = 0

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
q12 = data[11]

def start():
  print(" __      __       .__                               \n/  \    /  \ ____ |  |   ____  ____   _____   ____  \n\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ \n \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ \n  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >\n       \/       \/          \/            \/     \/ ")
  print("This is a quis on Pseudocode and Flowcharts.\n\n")
start()

f.close