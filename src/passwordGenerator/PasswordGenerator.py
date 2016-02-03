'''
Created on Feb 1, 2016

@author: f
'''
import random
def main():
    rand = random.SystemRandom
    inFile = open("../dict.txt","r")
    choose=""
    for line in inFile:
        choose+=line+", "
    choose=choose.replace("\n", "")
    choose = choose.split(", ")
    pw=""
    for i in range (0,4):
        pw+=choose[int(rand.random(rand)*(len(choose)+1))]+" "
    print("Your random password is: ", pw)


main()