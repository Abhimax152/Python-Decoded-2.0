secret_word = "python"

while True:
    word = input("Enter the secret word: ").lower()
    if word != secret_word:
        print("Try again")
    else:
        print("You got it!")
        break
