import random
def quiz(target):
    c = 0
    while(True):
        guess = int(input("Guess a number-> "))
        if(guess == target):
            print("Correct Guess")
            break
        elif(target<guess):
            print("Guess Lower")
        elif(target>guess):
            print("Guess Higher")

def Main():
    target = random.randint(1,100)
    quiz(target)

if __name__ == "__main__":
    Main()