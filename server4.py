#TCP
import time, socket, sys
import csv 
from xmlrpc.server import ServerHTMLDoc
from _thread import *
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
Threadcount=0 #thread count
new_socket.bind((host_name, port)) #yes

print("Server IP: ", s_ip)

name = "GROFERS"
print("---------GROFERS-------- ")

new_socket.listen(5) #yes

item_count=[3,4,5] #count of items present
 
dic={}
shop=["Potato","Onion","Coconut"]
cbasket=[] #storing the entire list
fields = ['Name', 'Phone Number', 'Address']
filename = "clients.csv"
    
with open(filename, 'a') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
def thread_client(conn):

    #sending server name
    conn.sendall(name.encode())
    
    #client name:
    client = (conn.recv(1024)).decode()
    print("\n\n"+client + ' has connected.')
    i=0

    #receiving number
    client1 = (conn.recv(1024)).decode()
    #print(client1 + ' number has connected.')


    #client address
    client_addr=(conn.recv(1024)).decode()
    #print("Address",client_addr)

    List=[client,client1,client_addr]   
    fields = ['Name', 'Phone Number', 'Address']
    filename = "clients.csv"
    
    with open(filename, 'a') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        #csvwriter.writerow(fields) 
        csvwriter.writerow(List)
    clientbasket=[0,0,0] #specific to one client
    

    print("The item count available today at the store are: ",item_count)
    clientactive=(conn.recv(1024)).decode()
    clientactive=int(clientactive)
    #print("Active status:",clientactive)
    while(clientactive):
        #User's choice
        cchoice=(conn.recv(1024)).decode()
        flag=1

        if(cchoice=="a"):
            itemselected=(conn.recv(1024)).decode()
            itemselected=int(itemselected)
            print("\nItem selected by client are: \n")
            if(item_count[itemselected -1] > 0):
                item_count[itemselected -1]=item_count[itemselected -1]-1
                mes="Item successfully added to the cart!!"
                clientbasket[itemselected -1]=clientbasket[itemselected -1]+1
                #print("\nItems in client cart: ",clientbasket)
                for i in range(3):
                    if(clientbasket[i] !=0):
                        print(shop[i],"::",clientbasket[i])
                conn.send(mes.encode())
                flag=1
            else:
                mes="\nItem unavailable!!"
                conn.send(mes.encode())
                flag=0
            flag=str(flag)
            conn.send(flag.encode())
            print("\nItems remaining at the store: ",item_count)
            for i in range(len(item_count)):
                print(shop[i],":",item_count[i])
            print("------------------------------------------------------------------------------------")
    
        elif(cchoice=="b"):
            itemtoreturn=(conn.recv(1024)).decode()
            itemtoreturn=int(itemtoreturn)
            if(clientbasket[itemtoreturn -1]!=0):
                item_count[itemtoreturn -1]=item_count[itemtoreturn -1]+1
                mes="Item returned succesfully!!"
                clientbasket[itemtoreturn -1]=clientbasket[itemtoreturn -1]-1
                print("Client basket :",clientbasket)
                for i in range(3):
                    if(clientbasket[i] !=0):
                        print(shop[i],"::",clientbasket[i])
                print("\nItems remaining at the store: ",item_count)
                for i in range(len(item_count)):
                    print(shop[i],":",item_count[i])
            elif(clientbasket[itemtoreturn-1]==0):
                print("Current client basket contents: ",clientbasket)
                mes="Invalid item!! We return only selected items!!"
            conn.send(mes.encode())


        elif(cchoice=="c"):
            clientactive=0
    cbasket.append(clientbasket)
    #print("Clientbasket",clientbasket)
    #print("cbasket",cbasket)
    #dic.update({client: clientbasket})
    #print("dic=",dic)
    price=[60,50,40]
    #print("Clientbasket:",clientbasket)
    print("Cbasket",cbasket)
    bill=0
    k=0
    for i in clientbasket: 
        bill=bill+i*price[k]
        k=k+1
    conn.send(str(bill).encode())
    dic.update({client: bill})

    print("dic=",dic)
    
    
    conn.close()

while True:
    conn, add  = new_socket.accept()#comes in while loop
    #print("Received connection from user with name: ", add[0])

    #print('Connection Established. Connected From: ',add[0])
    start_new_thread(thread_client,(conn,))
    Threadcount=Threadcount+1
    print("client number:",Threadcount)
new_socket.close()













