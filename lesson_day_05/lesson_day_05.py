# print('python files')
# fhand=open('./data/mbox-short.txt')
# count=0

# for line in fhand:
#     count=count+1

# print("Line Count:", count)

#fhand 
# first_line=''
# with open('./data/mbox-short.txt') as f:
#     first_line=f.readline()
# print(first_line)

# #
# fhand=open('./data/mbox-short.txt')
# inp=fhand.read()
# print(len(inp))

# print(inp[:50])

#Дахиад файлаа унших гээд үзье.
# print(len(fhand.read()))

#бүгдээрээ одоо файлаасаа үг эсвэл үсэг хайя
# fhand=open('./data/mbox-short.txt')
# for line in fhand:
#     if line.startswith('From'):
#         print(line)
    
# #
# fhand=open('./data/mbox-short.txt')
# for line in fhand:
#     line=line.rstrip()
#     if line.startswith('From'):
#         print(line)
#         continue
#     print(line)

#String-н find функц шиг хайцгаая
# fhand=open('./data/mbox-short.txt')
# for line in fhand:
#     line=line.rsplit()
#     if line.find('@uct.ac.za')== -1:
#         continue
#     print(line)

#Input ашиглая
    
# fname=input('Enter the file name:')
# fhand=open(fname)
# count=0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count=count+1
# print('There were ', count,'subject lines in ', fname)

# Try , catch ,except ашиглаж файлнуудыг байхгүй бол түүнийг алдаа гаргахгүйгээр handle хийдэг больё
# fname=input('Enter the file name:')
# try:
#     fhand=open(fname)
# except:
#     print('Enter cannot be openned:',fname)
#     exit()
# count=0 
# for line in fhand:
#     if line.startswith('Subject:'):
#         count=count+1
# print('There were ', count,'subject lines in ',fname)

#Одоо бид нар 

fout=open('./data/output.txt','w')
print(fout)
line1="This here's the wattle,\n"
fout.write(line1)
line2='the emblem of our land.\n'
fout.write(line2)
fout.close()
