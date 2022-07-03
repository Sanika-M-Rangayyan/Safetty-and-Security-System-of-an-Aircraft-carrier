#FINALLLL

import time, socket, sys
    
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
socket_server.connect((server_host, sport))
#print('This is your IP address: ',ip)
server_host = input('Enter server\'s IP address:')

#recieving server name
server_name = socket_server.recv(1024)
server_name = server_name.decode()



name = input('Enter your name: ')
#sending client name
socket_server.send(name.encode())
user_number=input("Enter your phone number: ") 
 
    
#number part
socket_server.send(user_number.encode())

#Client address
c_addr=input("Enter address:")
socket_server.send(c_addr.encode())

#Options
print("You are now connected with GROFERS")
print("\nWelcome to GROFERS!")
print("Hello "+name+"!!"+"\nPlease select an item to be added to the shopping cart- ")
print("1.Potato\tRs 50 \n2.Onion         Rs 80 \n3.Coconut\tRs 25")

clientactive=1
clientactive=str(clientactive)
socket_server.send(clientactive.encode())
clientactive=int(clientactive)
while(clientactive):
    #Taking choice of user:
    print("\nWhat would you like to do?")
    choice=input("a:Shop\nb:Return\nc:Exit\nCHOICE::\n")
    socket_server.send(choice.encode())

    if(choice=="a"):
        itemval=(input("Your item:"))
        socket_server.send(itemval.encode())
        mess=(socket_server.recv(1024)).decode()
        print(mess) #printing confirmation message
        #receiving flag
        flag=(socket_server.recv(1024)).decode()
        flag=int(flag)
        print(flag)
    elif choice=="b":
        itemret=input("Enter item:")
        socket_server.send(itemret.encode())
        mess=(socket_server.recv(1024)).decode()
        print(mess) #printing confirmation message
    elif choice=="c":
        clientactive=0
        bill=(socket_server.recv(1024)).decode()
        bill_final=int(bill)
        print("Your total bill is Rs ",bill_final)
        print("\n\nThank you for shopping with us!! Shop again soon!!\n")

socket_server.close()















'''
#Taking choice of the user:
option=input("select a to shop b to return")
socket_server.send(option.encode())






if(option=="a"): 
#print(server_name,' has joined ...')
    while True:
    
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)
        message = input("You : ")
        socket_server.send(message.encode()) 
        if(message=="y"):
            print("Your order is confirmed")
            #exit()
        if(message=="n"):
            print("Do shop with us sometime soon!!")
            exit()
        print("Thank you for shopping with us "+name+" !! :))")
if(option=="b"):
    while True:
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)
        message = input("You : ")
        socket_server.send(message.encode()) 
        if(message=="y"):
            print("return done")
            #exit()
        if(message=="n"):
            print("Okay")
            exit()
        print("Thank you for shopping with us "+name+" !! :))")
'''