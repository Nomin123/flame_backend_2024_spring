#Exercise 1

# fhand=open('./data/mbox-short.txt')

# for line in fhand:      
    
#     print(line.upper())

# #Exercise 2
#     sum=0
#     count=0
#     number=0
# name = input('Enter your filename:')
# fhand=open(name)
# for line in fhand:
#     if line.startswith('X-DSPAM-Confidence:'):
#         pos = line.find(':')
#         host = line[pos+1:]
#         number = float(host)
#         count=count+1
#         sum = sum + number
# average=sum/count
# print('Average spam confidence:',average)

#Exercise 3
fileName=input('Enter the file name:')

count=0
try:
    if fileName=='na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkd!')
    else:
        fhand=open(fileName)
        for line in fhand:
            count=count+1
        print('There were ',count, 'subject lines in ',fileName)    
except:
    print('File cannot be opened:',fileName)

