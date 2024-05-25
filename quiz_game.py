print("Welcome to my computer quiz!")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Okay! Lets play")
score =0
answer = input("What does CPU stand for ?").lower()
if answer == "central processing unit":
    print("! correct answer ")
    score += 1
else:
    print("Better Luck Next time!")
    
answer = input("What does GPU stand for ?").lower()
if answer == "graphic processing unit":
    print("! correct answer ")
    score += 1
else:
    print("Better Luck Next time!")
    
answer = input("What does ROM stand for ?").lower()
if answer == "read only memory":
    print("! correct answer ")
    score += 1
else:
    print("Better Luck Next time!")
    
answer = input("What does PS stand for ?").lower()
if answer == "power supply":
    print("! correct answer ")
    score += 1
else:
    print("Better Luck Next time!")
    
print ("You got " + str(score) + " questions correct!")