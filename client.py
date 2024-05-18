import socket


server_ip= "127.0.0.1"
port_number= 8084

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_ip,port_number))

while True:
    print("Give inputn like: 1 + 2 or type end to close ")
    data= input("Enter the operation you want to perform")

    if data=="end":
        client.send(data.encode())
        break

    client.send(data.encode())

    answer= client.recv(1024)

    display_answer= answer.decode()
    
    print(display_answer)

client.close()



