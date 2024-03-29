#dasgal 1

# eng2mn=dict()
# fhand=open('./data/word.txt')
# print(eng2mn)
# eng2mn['father']='аав'
# eng2mn['mother']='ээж'
# print(eng2mn)
# print(len(eng2mn))

# print(eng2mn.keys())
# for key in eng2mn.keys():
#     print(key)

# print(eng2mn.values())
# for value in eng2mn.values():
#     print(value)

# fname=open('./data/word.txt')
# eng2mn=dict()

# for line in fname:
#     #
#     words=line.split()
#     for word in words:
#         eng2mn[word]='1'
#         print(eng2mn)
    
#Dasgal 2
fname=open('./data/mbox-short.txt')
date=dict()

for line in fname:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            day=words[2]
            if day not in date:
                date[day]=1

            else:
                date[day] =date[day]+ 1

print(date)

#Dasgal 3

fname=open('./data/mbox-short.txt')
address=dict()

for line in fname:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            email=words[1]
            if email not in address:
                address[email]=1
            else:
                address[email]+=1
            

print(address)

#Dasgal 4
fhand=input('Enter a file name:')
fname=open(fhand)
address=dict()
count=0


for line in fname:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            email=words[1]
            if email not in address:
                address[email]=1
            else:
                address[email]+=1
                if count<address[email]:
                    count=address[email]
                    name=email




print(name,count)

#Dasgal 5

hand=input('Enter a file name:')
fname=open(fhand)
domain=dict()
count=0

for line in fname:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            email=words[1]
            dom=email.split('@')
            if dom[1] not in domain:
                domain[dom[1]]=1
            else:
                domain[dom[1]]+=1

print(domain)






