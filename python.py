print("hi")

name= input("Hello person. what is your name?")
Health= input("You start off with 10 health (Click Enter to view the next prompt")
response = input("Hello " + name + "! You are stuck in space you can only continue your journey if you pick the right card- Card (1 or 2) ")

if response == "1":
    print("You hit an asteroid You lost one health!!!!" +   name)
if response == "2":
    print("Great! you survived that challenge!" +   name)


Challenge = input("Now you have reached the next challenge. There are two paths which one are you going on? (Left or Right)")
if Challenge == "Left":
    print("Great! you went on the right path!" + name)
if Challenge == "Right":
    print("You tripped on a rock and you lost one health" +  name)
Food = input("You are now hungry, What are you going to eat (Oreo or the Apple)")
if Food == "Apple":
    print(" You eat the right food! " + name)
if Food == "Oreo":
    print(" You eat the oreo with poison inside, " + name)