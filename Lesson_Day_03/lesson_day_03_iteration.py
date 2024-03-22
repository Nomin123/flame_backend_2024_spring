print('lesson day python iteration')
print('While statement')


n=5
while n>0:
    print(n)
    n=n-1
print('Blasstoff')


while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('The End!-1')


while True:
    line==input('>')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('The End!-2')


friends=['Joseph','Glenn','Sally']

for friend in friends:
    print('Happy New Year:', friend)
print('Done')

#counting and summing with FOR loops
count=0
for element in [3,41,12,9,74,15]:
    count=count+1
print('Count:',count)

#total of the element sum
total=0
for element in[3,41,12,9,74,15]:
    total=total+element
print ('Total',total)








