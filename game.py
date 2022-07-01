
from os import stat

class Game:
    def __init__(self):
        while True:
            print('''
            Welcome
            1:multiplication table
            2:count of words in sentance
            3:exit
            ''')
            userchoice=int(input("Enter your choice: "))
            if int(userchoice)==3:
                break
            elif userchoice==1:
                start=int(input("enter the start: "))
                end=int(input("enter the end: "))
                self.multiblication_table(start,end)
            elif userchoice==2:
                sentance=input('enter the sentance:')
                self.countWordsAndLETTERS(sentance)
            playagain=input('press any key to play again if ypu want to exit presss n:')
            if playagain=='n':
               break
    def multiblication_table(self,start,end):
        for x in range(start,end+1):
            for m in range(1,11):
                print(f'{x}*{m}={x*m}')   
            print('-----------------')
    def countWordsAndLETTERS(self,Sentance):
        countwords=len(Sentance.split())
        print(f'the count of words is:{countwords} ')
        return countwords
        

g1=Game()















       



