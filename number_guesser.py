import random
toprange= input("Enter a number")
if toprange.isdigit():
    toprange= int(toprange)

    if toprange <= 0:
        print("Please type a number larger than 0 next time")
        quit()

else:
    print("Please type a number next time")
    quit()
    
r = random.randint(0,toprange)
guesses = 0
while(1):
    guesses += 1
    user_guess = input("Make a guess !")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if r == user_guess:
        print("You got it !")
        break
    elif(r < user_guess):
        print("You are above the number")
    else:
        print("You are lower the number")
        
print("You Got it in", guesses, "Guesses")