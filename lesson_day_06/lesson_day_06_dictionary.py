# print('pothon dictionary.py')
# #father-аав
# # a=[1,2,3,4,5,6]

# # print(a.find(6))# 5 удаа хайгаад байна хамгийн удахдаа : секунд



# # eng2mn=dict()
# print(eng2mn)
# eng2mn['father']='аав'
# print(eng2mn)


# #эгч ах дүү эмээ өвөө гэдэг үгнүүдийг dictionary дээрээ нэмнэ үү
# eng2mn['sister']='эгч'
# eng2mn['brother']='ах'
# eng2mn['grand mother']='эмээ'
# eng2mn['grand father']='өвөө'
# print(len(eng2mn))
# print(eng2mn(['father']))
# print(eng2mn(['grand father']))
# print(eng2mn.values())

# # Файл дотор хадгалагдсан байгаа үгнүүдийг тоолдог
# fname=input('Enter the file name:')
# try:
#     fhand=open(fname)
# except:
#     print('File cannot be opened')



















#looping in dictionaries

names={'chuck':1,'annie':42,'jan':100}
for key in names:
    print(key ,names[key])

counts={'chuck':1,'annie':42,'jan':100}
for key in counts:
    if counts[key]>10:
        print(key,counts[key])

import string
print(string.punctuation)

fname=input('Enter the file name')
try:
    fhand=open(fname)
except:
    print('File can not be opened:',fname)
    exit()

counts=dict()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

print(counts)