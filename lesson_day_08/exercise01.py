#Dasgal 1

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fname=input('Та хаягаа оруулна уу?')



try:
    domain=fname.split('/')
    print(domain[2])
    
    mysock.connect((domain[2], 80))
    cmd = f'GET {fname} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        print(data)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
except:
    print('URL is not founded!')
    exit()

#Exercise 2










