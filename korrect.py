#coding: utf-8
#@Author: Arthur PONS -> github.com/unguest
import os

def levDist(str1, str2):
	lDist = 0
	for i in (range(min(len(str1), len(str2)))):
		if str1[i] != str2[i]:
			lDist += 1
	lDist += len(set(str1) - set(str2))
	return lDist



def korrect(word, dico):
	with open(str(dico), "r") as f:
		for word1 in f:
			dist = levDist(word, word1)
			if dist <= len(word) / 4:
				print("Would you either say {} ?".format(word1))
			else:
				continue
if __name__ == "__main__":
	word = input("Put a word : ")
	while len(word) == 0:
		word = input("Put a word : ")

	dicN = input("Path to the dico : ")
	while len(word) == 0:
		dicN = input("Path to the dico : ")
	korrect(word, dico)
