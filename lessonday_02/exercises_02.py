#dasgal 1

# hours=int(input('Enter Hours:'))
# rate=int(input('Enter Rate:'))
# if(hours>40):
#     pay=40*rate+(hours-40)*1.5*rate
#     print(pay)
# else:
#     pay=hours*rate
#     print(pay)

# #dasgal 2
    
# try:
#     hours=input('Enter Hours:')
#     rate=input('Enter Rate:')
#     if(hours>40):
#         pay=40*rate+(hours-40)*1.5*rate
#         print(pay)
#     else:
#         pay=hours*rate
#         print(pay)
# except:
#     print('Error, please enter numeric input')

#dasgal 3
    
try:
    score=float(input('Enter score:'))
    if(0<=score<0.6):
        print('F')
    elif(0.6<=score<0.7):
        print('D')
    elif(0.7<=score<0.8):
        print('C')
    elif(0.8<=score<0.9):
        print('B')
    elif(0.9<=score<1.0):
        print("A")
    else:
        print('Bad score')
except:
    print('Bad input')