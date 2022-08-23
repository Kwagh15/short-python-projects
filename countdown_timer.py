import time
#creating a function
def countdown(t):
    while t>0:
        print(t)
        t=t-1
        time.sleep(1) #time difference between countdown seconds
    print("Time's up....")

print("How many seconds to countdown ?Enter an integer.")
second=input()
#exception handled
while not second.isdigit():
    print("That wasn't an integer number!Please Enter an Integer number")
    second=input()

second=int(second)   #created an object
countdown(second)  #called the function using object reference