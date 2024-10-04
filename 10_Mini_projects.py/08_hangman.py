f_person = input("Enter and word : ")
display = []
lives = 6
for letter in f_person:
    display += '_'

print(display)
while True:
    user = input("Guess a letter: ").lower()

    if user in f_person:
        for position in range(len(f_person)):
            if f_person[position] == user:
                display[position] = user
        print(display)
    else:
        print("You guessed wrong.")
        lives -= 1
        print(f"Now you have only {lives} attempts left.")

    if lives == 0:
        print("----------YOU FAIL----------")
        break

    if "_" not in display:
        print("----------YOU WIN----------")
        break
