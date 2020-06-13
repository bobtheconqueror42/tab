
import pyautogui
import time
print ("this will open a new wab in your browser and close the first one")
a = input("how many times")

a = int(a)

print ('open browser in')

print ('15')
time.sleep(1)
print ("14")
time.sleep(1)
print ("13")
time.sleep(1)
print ("12")
time.sleep(1)
print ("11")
time.sleep(1)
print ("10")
time.sleep(1)
print ("9")
time.sleep(1)
print ("8")
time.sleep(1)
print ("7")
time.sleep(1)
print ("6")
time.sleep(1)
print ("5")
time.sleep(1)
print ("4")
time.sleep(1)
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1")
time.sleep(5)



pyautogui.keyDown('ctrl')

i = 0

while i < a:
    
    pyautogui.press('t')
    time.sleep(.1)
    pyautogui.press('1')
    time.sleep(.1)
    pyautogui.press('w')
    time.sleep(.1)
    a = a - 1
    print (a)
pyautogui.keyUp('ctrl')