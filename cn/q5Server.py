from socket import *
serverName=gethostname()
serverPort=12001
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("The Server is ready to recieve")
while(1):
    count=0
    conn,addr=serverSocket.accept()
    file2=conn.recv(1024).decode()
    list1=[]
    list1=file2.split(" ")
    file=open(list1[0],"r")
    print("file to search: ",list1[0])
    print("word to search: ",list1[1])
    words=file.read(1024)
    list2=[]
    list2=words.split(" ")
    print("words in file: ")
    print(list2)
    print("counting the words....")
    for i in list2:
        if(list1[1]==i):
            count+=1

    print(count)
    conn.send(str(count).encode('utf8'))
    print("data sent to client!")
    break
file.close()
conn.close()
