def languageCheck():
    language=input("choose your lenguage: ")
    if language=="hy":
        for i in open("hyGreeting.txt"):
            print(i,end="")
        print("")
    elif language=="ru":
        for i in open("ruGreeting.txt"):
            print(i, end="")
        print("")
    elif language=="en":
        for i in open("enGreeting.txt"):
            print(i, end="")
        print("")
    else:
        print("try again")
        languageCheck()
languageCheck()
