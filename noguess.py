import random
print("-"*150)
text=" Welcome to the Random number guessing game 🎯"
print(text.center(150))
print("-"*150)
Name= input('Enter your name: ')
print("Choose Game Mode: ")

print("1. Easy Mode (10 attempts)")
print("2. Hard Mode (5 attempts)")
r=random.randint(1,100)
choice = input("Enter your choice (1,2): ")
if choice == '1':
    attempts=10
elif choice == '2':
    attempts = 5
else:
    print("Enter a valid choice,")
print ("Welcome" , Name,"!"," ","Guess the number between 1 and 100. ")
while attempts>=0:
    score = 0
    score= attempts*10 
    guess = int(input("Enter your guess: "))
    
    if r==guess:
        print("You won.🎉 /n Your score is: ", score)
        break
    elif r<guess:
        print("Go for lower no.")
    elif r>guess:
        print("Go for Higher no.")
    
    attempts-=1
    print("Attempts left", attempts)
    
if attempts==0:
    print("Game lost😥.","Have better luck next time.")
    print("The random no. is: ", r)
print("<----------------Scoreboard---------------->")
print(Name ,"Scored ",score,"points.")
print("--- Thanks for playing Random number guessing game --- ")