eng_to_loj = {"greet": "rinsa", "red": "xunre", "sad": "badri", "happy": "djugei", "programmer": "sampla", "human": "remna", "hate": "xebni", "language": "bangu"}

def intro():
    print("Welcome to the English to Lojban Dictionary!")
    print("Remember, there are no nouns in Lojban,\nYou must convert verbs to nouns using the particals 'lo' and 'ku'")

def info():
    print("Lojban is a constructed language designed to be grammatically unambiguous")
    print("For more information, go to https://mw.lojban.org/papri/Lojban")

def example():
    print("Ex: lo mlatu ku pinxe lo ladru ku")
    print("English: The cat drinks milk")
    print("Literally: (noun) to be a cat drinks (noun) to be milk")

while 1:
    print("")
    op = int(input("[0] English To Lojban\n[1] Lojban To English\n[2] More Information\n[3] Example\n"))
    if op == 0:
        word = input("Input Word (No Uppercase Letters): ")
        if word in eng_to_loj:
            print(f"{word} is {eng_to_loj[word]} in lojban\n")
        else:
            print("Word not found!\n")
    elif op == 1:
        res = ""
        word = input("Input Word (No Lower Case): ")
        for key in eng_to_loj:
            if eng_to_loj[key] == word:
                res = key
                print(f"{word} is {res} in English\n")
                break;
        else:
            print("Word not found!")   
    elif op == 2:
        info()
    elif op == 3:
        example()
    op = int(input("\n[0] Continue\n[1] Exit\n"))
    if op != 0:
        break;