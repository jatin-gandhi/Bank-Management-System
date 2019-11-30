#include<iostream>
#include<unistd.h>
#include<stdlib.h>
using namespace std;
#define bucketsize 256
void bktinput(int a, int b);
int main()
{
int op,pktsize[]={100, 345, 230,78, 980, 130, 7, 89, 670, 256};
cout<<"Enter output rate:";
cin>>op; //50(Mbps)
for(int i=0;i<10;i++)
{
usleep(rand()%1000);
cout<<"\nPacket no"<<i+1<<"\tPacket size="<<pktsize[i];
bktinput(pktsize[i],op);
}
return 0;
}
void bktinput(int a,int b)
{
if(a>bucketsize)
cout<<"\n\t\tBucket overflow";
else{
usleep(500);
while(a>b)
{
cout<<"\n\t\t"<<b<<"bytes outputted";
a-=b;
usleep(500);
}
if(a>0)
cout<<"\n\t\tlast"<<a<<"bytes sent\t";
cout<<"\n\t\t Bucket output successful";
}
}
/*
import time
import random
bucketSize =512
def bktInput(size,rate):
    if size>bucketSize:
        print("\n Bucket Overflow")
    else:
        time.sleep(1)
        while size>rate:
            print("\n {} bytes sent".format(rate))
            size -=rate
            time.sleep(1)
        if size >0:
            print("\n Last {} bytes sent".format(size))
        print("\n Bucket output successful")

outputRate = int(input("Enter the ouput rate : "))
for i in range(5):
    print(random.randint(0,1000))
    time.sleep(random.randint(0,1000))
    packetSize = random.randint(0,1000)
    print("\n Packet Number : {}  \n Packet Size : {} ".format((i+1),packetSize))
    bktInput(packetSize,outputRate)
    
    */