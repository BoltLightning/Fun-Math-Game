print("Welcome to Bolt's Fun Math Game! the goal of this game is to test your math skills!")
print("Answer these questions to advance to the next set, They will get progressivaly harder!")
print("This game will test many types of math including: Addition, Subtraction, Multiplcation and division!")
print("NOTICE: There are no commas in the answers 1000 or larger, so answer '1000' instead of '1,000' This program is very case sensative, getting anything incorrect will close the terminal automatically")
print("Be sure to follow Boltlightning780 on Youtube!")


Getstarted = input("Type 'Start' To begin! [be aware this is case sensative so be sure to have capital letters when needed]")

if(Getstarted == "Start") :
    print("ALright, Addition:")
else :
    print("Exiting game."); 
    quit()
#Addition Section
question1 = input("Try This one! 58+25")

if(question1 == "83") :
    print("Correct!")
else :
    print("Sorry, that is incorrect, exiting game!")
    quit()

question2 = input("Try this one! 121+65")

if(question2 == "186") :
    print("That's correct! Great Job! keep it up!")
else :
    print("Sorry, that is not correct! Exiting game...")
    quit()

question3 = input("Try This one! 283+65+32")

if(question3 == "380") :
    print("That's correct! You're good at this aren't you! :)")
else : 
    print("Unfortunatly that is not correct, You'll get it next time! Exiting game...")
    quit()

question4 = input("Try this one! 854 + 123 + 69")

if(question4 == "1046") :
    print("That's right! Wow! you're doing solid!")
else :
    print("Oh no! that was not the correct answer! Exiting game...")
    quit()
    


question5 = input("1285+218+777")

if(question5 == "2280") :
    print("That's correct! Congradulations! You have completed the addition portion!")
else :
    print("Sorry, but that is incorrect. Exiting game...")
    quit()

continue1 = input("Type 'Ready' To move on to the subtraction section!")

if(continue1 == "Ready") :
    print("Fetching question...") 
else :
    print("Exiting Game...")
    quit()

#Subtraction Section of game

question1b = input("Try this one! 64-13")

if(question1b == "51") :
    print("That's correct! Great job!")
else :
    print("Sorry, that is not correct. Exiting game...")
    quit()

question2b = input("Give this one a shot! 100-63")

if(question2b == "37") :
    print("Awesome job! keep it up!")
else :
    print("Sorry, that is incorrect, Exiting game...")
    quit()

question3b = input("Try this one! 241-172")

if(question3b == "69") :
    print("Nice! you got it!")
else :
    print("Sorry, that is incorrect, Exiting game...")
    quit()

question4b = input("Give this one a shot! 747-737-28")

if(question4b == "-18") :
    print("That's right! You're doing great!")
else :
    print("Sorry, that is incorrect, exiting game...")


question5b = input("Try this one! 858-124-62-88")

if(question5b == "584") :
    print("That's correct! Wow! You have completed the subtration section!")
else :
    print("Sorry, that is incorrect. Exiting game")
    quit()

continue2 = input("Type 'Ready' to move on to the multiplcation section!")

if(continue2 == "Ready") :
    print("Fetching questions")
else :
    print("Exiting Game")
    quit()

question1c = input("Try this one! 5x6")

if(question1c == "30") :
    print("That's correct! Awesome job!")
else :
    print("Sorry that is not correct, Exiting game...")
    quit()

question2c = input("Try this one! 13x8")

if(question2c == "104") :
    print("That's correct! Good job!")
else :
    print("Sorry that is incorrect, Exiting game")
    quit()

question3c = input("Try this one! 15x12")

if(question3c == "180") :
    print("That's right! Great job!")
else :
    print("Sorry, that is incorrect, Exiting game") 
    quit()

question4c = input("Give this one a shot! 123x24")

if(question4c == "2952") :
    print("Wow! that's correct! you're doing solid!")
else :
    print("Sorry, that is incorrect, exiting game...")
    quit()

question5c = input("Try this one! 154x218")

if(question5c == "33572") :

    print("WOW! that was a tough one yet you got it! Great job! You have finished the multiplcation section!")
else :
    print("Sorry, that was a tough one, but that was incorrect, exiting game")
    quit()

continue3 = input("Type 'Ready' to move on to the final division section!")

if(continue3 == "Ready") :
    print("Fetching questions...")
else :
    print("Exiting game...")
    quit()

question1d = input("Give this one a shot! 125/5")

if(question1d == "25") :
    print("That's correct! Awesome!")
else :
    print("Sorry, that is not correct, exiting game")
    quit()

question2d = input("Try this one! 510/6")

if(question2d == "86") :
    print("That's correct! Great job!")
else :
    print("Sorry that is not correct, exiting game...")
    quit()


question3d = input("Try this one! 522/20")

if(question3d == "26.1") :
    print("That's correct! do note, any decimals will be rounded to the nearest hundreths (x.xx)")
else :
    print("Sorry, that is incorrect, Exiting game")
    quit()

question4d = input("1562/32")

if(question4d == "48.81") :
    print("That's correct! Great job! Almost done! ;)")
else :
    print("Sorry, that is incorrect, exiting game...")
    quit()

print("One last question! Ready for it! here it is!")

question5d = input("Give this last one a shot! 3712/142")

if(question5d == "26.14") :
    print("That's correct! Amazing!")
else :
    print("Sorry, That is incorrect, exiting game...")

print("Wow! You completed all the questions! I hope you enjoyed this fun game! If you did, please subscribe to me at my youtube Boltlightning780, Twitter @Bolt2434, IG, @bolt_triple7")
print("This game was created using python, I'm currentally learning how to code in python and this is my first project! ")

Exitgame = input("Type Exit to exit game")

if(Exitgame == "Exit") :
    print("Exiting game...")
    quit()