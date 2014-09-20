from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    totalScore = 0
    newWord = ""
    for word in wordList:
        if isValidWord(word,hand,wordList):
            if totalScore < getWordScore(word, n):
                newWord = word
                totalScore = getWordScore(word, n)
    if newWord != "":
        return newWord
    else:
        return None
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalScore = 0
    while calculateHandlen(hand):
        print "Current Hand: ",
        displayHand(hand)
        newWord = compChooseWord(hand, wordList, n)
        if newWord != None:
            totalScore = totalScore + getWordScore(newWord, n)
            print '"',newWord,'"', "earned", getWordScore(newWord, n), "points. Total:",  totalScore , "points"
            hand = updateHand(hand, newWord)
            print
        else:
            break;
    if(calculateHandlen(hand) > 0):
        print "Total score: ", totalScore, " points."
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand = False
    while True:
        user_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_input == "n":
            hand = dealHand(HAND_SIZE)
            #tester1 = True
            while True:
                user_mode = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if user_mode == "u":
                    playHand(hand, wordList, HAND_SIZE)
                    #tester1 = False
                    break
                elif user_mode == "c":
                    compPlayHand(hand, wordList, HAND_SIZE)
                    #tester1 = False
                    break
                else:
                    print "Invalid command."
        elif user_input == "r":
            if hand:
                user_mode = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if user_mode == "u":
                    playHand(hand, wordList, HAND_SIZE)
                elif user_mode == "c":
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print "Invalid command."
            else:
                print "You have not played a hand yet. Please play a new hand first!"
        elif user_input == "e":
            break
        else:
            print "Invalid command."
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


