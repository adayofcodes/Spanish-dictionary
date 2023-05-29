#This is a basic spanish dictionary of sorts using python dictionaries

basic_spanish = {
    "take": "tomar",
    "run": "correr",
    "food": "comida",
    "thanks": "gracias"
}

medium_spanish = {
    "to be": ["ser", "soy"],
    "every": "cada",
    "less": "menos"
}

hard_spanish = {
    "idiosyncrasy": "idiosincrasia",
    "blender": "licuadora",
    "umbrella": "paraguas"
}

def easy(basic_spanish):
    print("Easy words:\n")
    for x in basic_spanish:
        print(x)
    
    choice = input("\nWhat word do you want to know the meaning of?\n\n")
    if choice in basic_spanish.keys():
        print(f"{choice} means {basic_spanish.setdefault(choice)} in spanish")


def medium(medium_spanish):
    print("Medium words:\n")
    for x in medium_spanish:
        print(x)

    choice = input("\nWhat word do you want to know the meaning of?\n\n")
    if choice in medium_spanish.keys():
        print(f"{choice} means {medium_spanish.setdefault(choice)} in spanish")

def hard(hard_spanish):
    print("Hard words:\n")
    for x in hard_spanish:
        print(x)

    choice = input("\nWhat word do you want to know the meaning of?\n\n")
    if choice in hard_spanish.keys():
        print(f"{choice} means {hard_spanish.setdefault(choice)} in spanish")

while True:
    word_difficulty = input("Word you like an easy, medium, or difficult Spanish word?\n")

    if word_difficulty == "easy":
        easy(basic_spanish)
    elif word_difficulty == "medium":
        medium(medium_spanish)
    elif word_difficulty == "difficult":
        hard(hard_spanish)

    keep_going = input("Would you like to continue? Yes or no\n\n")
    if keep_going.lower() != "yes":
        print("Goodbye")
        exit()

