import random
n = random.randint(1, 100)
a = -1
guesses = 0  # Initialize guesses counter
while a != n:
    guesses += 1 
    a = int(input("Guess a number: "))
    if a > n:
        print("Lower number please")
    elif a < n:  # Changed from else to elif to only show "Higher" when a < n
        print("Higher number please")

print(f"You have guessed the number correctly in {guesses} attempts")  # Fixed pluralization