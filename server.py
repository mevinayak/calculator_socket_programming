import socket


ip_address= "127.0.0.1"
port_number= 8084

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip_address,port_number))
server.listen(1)

print("server has started")

print("waiting for connection")

clientConnection, clientAddress= server.accept()
print(f"Current Client is {clientAddress}")

msg=""

while True:
    data= clientConnection.recv(1024)
    msg= data.decode()
    print(msg)
    if msg=='end':
        print("Connection ended")
        break

    message= msg.split(" ")
    if len(message)==3:
        item1= message[0]
        item2= message[2]
        operator= message[1]
    else:
        break


    if operator=='+':
        answer= int(item1)+int(item2)
    elif operator=='-':
        answer= int(item1)-int(item2)
    elif operator== '/':
        answer= int(item1)//int(item2)
    elif operator=='*':
        answer = int(item1)*int(item2)

    print("sending result to the client")

    clientConnection.send((str(answer)).encode())
clientConnection.close()



    
