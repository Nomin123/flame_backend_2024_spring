import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))#connect to the server

cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #make a request
mysock.send(cmd) #send the request
#http 80
while True:
    data=mysock.recv(512) #when server responded with data
    if len(data)<1:
        break
    print(data.decode(),end='')

mysock.close()# end of connection
