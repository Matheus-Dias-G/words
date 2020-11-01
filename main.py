import os
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
	    's', 't', 'u', 'v', 'w', 'y',
	    'z']
word = str(input('type a word: '))


x = 0
y = 0
v = False
words = []
while v == False:
	comp_word = ''.join(words)
	print(comp_word, alphabet[y])
	time.sleep(0.5)
	os.system('cls' if os.name == 'nt' else 'clear')
	if word[x] == alphabet[y]:
		words.append(alphabet[y])
		x += 1
		y = 0
	else:
		y += 1
	if x > len(word)-1:
		comp_word = ''.join(words)
		print(comp_word)
		break
