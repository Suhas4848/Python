 #GUESS THE NUMBER GAME                    
import random
a=input("Enter the top number ")
guess = 0

if a.isdigit():
        a = int(a)
else:
        print("please enter the number only!")      
        quit() 
while True:
    guess+=1    
    r = random.randrange(0,a)
    x = int(input("Enter the guess "))    
    if r==x:
        print("Guess is correct!",x,"==",r)
        break
    
    else: 
        if r>x:
            print("your no is below the random no ",r)
        else :
            print("your no is above the random no ",r)  
         
    if r !=x:
        print("Guess is incorrect ",x,"!=",r) 
       
    continue         

print("Congaratulations!!!! after",guess,"guesses answer is correct") 
   
   