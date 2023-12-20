# Python program for Finite Automata
# Stop Word Removal Algorithm

import numpy as np

# Function to generate an array of string from any text
def splitsen(my_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char

    # display the unpunctuated string
    l = no_punct.split()
    return l

# This Function checks if a word belongs to the FA (is a stop word)
def checkFA(word, n, FA, k):
	state = 0
	word = word.lower()
	
	for i in range(n):
		if word[i] in k.keys():
			state = FA[state][k[word[i]]]

		else:
			t = 10
			state = FA[state][t]

	
	return checkState(state)

# This Function checks if the current state is the final state
def checkState(state):

	array = [1, 2, 4, 5, 11]

	if (state in array):
		return True
	
	else:
		return False

# This Function removes the Stop words from a text
def removeStopWord(text, FA, k):
	arr = splitsen(text)
	
	i = 0

	while(i!= len(arr)):
		n = len(arr[i])
		if(checkFA(arr[i], n, FA, k)):
			arr.pop(i)

		else:
			i = i+1
		
	t = " ".join(arr)

	return t



# Driver program to test above function			
def main():

	k = {'t': 0, 'h': 1, 'e': 2, 'a': 3, 'r' : 4, 'n' : 5, 'd' : 6, 'o' : 7, 'f' : 8, 'w' : 9}

	FA = np.array([[6, 12, 12, 1, 12, 12, 12, 3, 12, 8, 12, 12],
	[12, 12, 12, 12, 7, 2, 12, 12, 12, 12, 12], 
	[12, 12, 12, 12, 12, 12, 4, 12, 12, 12, 12], 
	[12, 12, 12, 12, 4, 12, 12, 12, 5, 12, 12],
	[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
	[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 7, 12, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 12, 2, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 12, 10, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 12, 12, 12, 12, 11, 12, 12, 12, 12, 12], 
	[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
	[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]])


	text = "Hey,are you doing fine?"
	t = removeStopWord(text, FA, k)
	print(t)

if __name__ == '__main__':
	main()

