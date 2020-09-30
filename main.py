# 2020 September 23rd
import random
import grahpics
import os

def file_len(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
		

# Get the word
def getWord(word):
	word = list(word)
	obfWord = len(word) * '*'
	print(f"\033[95mChosen word: {obfWord}")
	return dict.fromkeys(word)


# Guess
def guess(guess, word):
    if guess in word:
        return True
    else:
        return False

def random_line(file):
    line = next(file)
    for num, aline in enumerate(file, 2):
      if random.randrange(num): continue
      line = aline
    return line

blacklistedWords = []

while True:
	# Avoid repeating words
	while True:
		randomLine = random_line(open("words.txt"))
		if randomLine in blacklistedWords:
			continue
		else:
			blacklistedWords.append(randomLine)
			break

	# Ask for getWord
	word = getWord(randomLine)

	chances = 0
	chancesMax = 6
	correct = 0
	guessedList = []
	usedWords = set()
	while True:
		inp = input("\033[1m\033[94m^ Enter the letter you want to guess: ")
		g = guess(inp, word)
		usedWords.add(inp)
		if g == True:
			if word[inp] == "True":
				print("\033[93m:( Letter was repeated (incorrect)!")
				print(grahpics.hangmen[chances - 6])
				chances += 1
			else:
				print("\033[92m:) Letter was correct!")
				word[inp] = "True"
				correct += 1
		else:
			print("\033[1m\033[91m:( Letter was incorrect!")
			print(grahpics.hangmen[chances - 6])
			chances += 1

		# Show word guessed so far
		obfWord = ""
		fmtWord = ''.join(word.keys())
		for x in range(len(fmtWord)):
			if fmtWord[x] in usedWords:
				obfWord += fmtWord[x]
			else:
				obfWord += "_"
		
		print(f"\033[95m? You completed this much of the word: {obfWord}")

		if correct >= len(word.keys()):
			print(f"\033[92m:) You won! The word was \"{''.join(word.keys())}\"")
			break
		if chances >= chancesMax:
			print(f"\033[91m:( You failed. The word was: '{''.join(word.keys())}'")
			break
		print(f"\033[95m? You have {chances} chances left, and {correct} correct.")
		print(f"\033[95m? You also have used these letters: {', '.join(usedWords)}")
		input("Continue? (press enter): ")
		os.system('clear')
	while True:
		playAgain = input("\033[94m^ Do you want to play again (Y/N)? ")
		if playAgain.upper() == 'Y':
			break
		elif playAgain.upper() == 'N': 
			quit()
		else:
			print("\033[93m:( Invalid input")