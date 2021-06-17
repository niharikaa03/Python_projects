import random 
list=['rock','paper','scissors']
x=random.choice(list)
y=(input("choose the action"))
if x=='rock' and y=='scissors':
    print("computer wins")
elif x=='paper' and y=='rock':
    print("computer wins")
elif x=='scissors' and y=='paper':
    print("computer wins")
else:
    print("user wins")