import random
import math


listOfWords = ['chair', 'animal', 'sidewalk', 'dinner', 'beach', 'flower']



def drawGuy(numberIncorrect):
    guyDrawing = ['  O',' _|_','/ | \\','  |', ' / \\', '/   \ ']
    
    for count in range(len(guyDrawing)-numberIncorrect):
        print guyDrawing[count]
        
    print ""
        
        
def printAnswer(playerIn):
    answer = ""
    
    for i in range(len(playerIn)):
       answer += playerIn[i]
    
    print answer
    
    
def drawAll(incorrectCount, player, badLtrs):
    print
    print "Incorrect Letters: " + badLtrs
    print
    drawGuy(incorrectCount)
    printAnswer(player)  
   
def main():
    
    print "Hangman"
    print "by Trevor and Justin"
    print "all items are typical things"
    
    randomNumber = random.randint(0,len(listOfWords)-1)
    badLetters = ""
    bPlaying = True
    incorrectCount = 0
    player = []
    for i in range(len(listOfWords[randomNumber])):
        player.append("_ ")
    
    while bPlaying:
        currentWord = listOfWords[randomNumber]
        bGameGoing = True
        while bGameGoing:
            #print currentWord
            drawAll(incorrectCount, player, badLetters)
            guess = raw_input('Please guess a letter!')
            guess = guess.lower()
            while (guess < 'a') or (guess > 'z'):
                guess = raw_input('Error: Please guess a letter!')
                guess = guess.lower() 
            
            bFound = False
            for i in range(len(currentWord)):
                if currentWord[i] == guess:
                    player[i] = guess + " "
                    bFound = True
            if bFound == False:
                incorrectCount = incorrectCount + 1
                badLetters = badLetters + guess + " "
            
            # stupid method for converting list to string
            checkAns = ""
            for i in range(len(player)):
                checkAns += player[i]
                
            # check if we should still be playing
            if incorrectCount > 5:
                bGameGoing = False
                print "You lose :("
            if checkAns.find("_") < 0:
                bGameGoing = False
                drawAll(incorrectCount, player, badLetters)
                print
                print "You win! :)"
        
        # after player has won or lost
        randomNumber = random.randint(0,len(listOfWords)-1)
        incorrectCount = 0;
        badLetters = ""
        player = []
        for i in range(len(listOfWords[randomNumber])):
            player.append("_ ") 
        result = raw_input("Press 'y' to continue playing!")
        if(result != 'y'):
            bPlaying = False
        
    print "Thank you for playing!"

main()