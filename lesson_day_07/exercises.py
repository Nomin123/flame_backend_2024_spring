#Example

import string
fhand=open('./data/romeo-full.txt')
counts=dict()
for line in fhand:
    line =line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
lst=list()
for key,val in list(counts.items()):
    lst.append((val,key))

lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)

#Exercise 1

fhand=open('./data/mbox-short.txt')
address=dict()

for line in fhand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            email=words[1]
            if email not in address:
                address[email]=1
            else:
                address[email]+=1

# print(address)

lst=list()
for key,val in list(address.items()):
    lst.append((val,key))

lst.sort(reverse=True)
print(lst[0])

print(lst)

#Exercise 2

fhand=open('./data/mbox-short.txt')
time=dict()


for line in fhand:
    if line.startswith('From'):
        words=line.split()
        # print(words)
        if len(words)>2:
            hour=words[5].split(':')
            print(hour[0])

            tsag=hour[0]

            if tsag not in time:
                time[tsag]=1
            else:
                time[tsag]+=1
        
# print(time)
li=list(time.items())


li.sort()
for v in li:
    print(v)


#Exercise 3
    
fhand=open('https://gogo.mn/r/vxed0')
text=dict()

for line in fhand:
    line =line.translate(line.maketrans('','',string.punctuation))
    line =line.translate(line.maketrans('','',string.digits))
    line=line.lower()
    words=line.split()
    for word in words:
        for letter in word:
            print(letter)
            if letter not in text:
                text[letter]=1
            else:
                text[letter]+=1
list=text
print(list)








        
    



    






              

            
            
            





