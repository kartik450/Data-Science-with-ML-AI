import socket as sk

def send():
    s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
    ip=input("Enter ip address: ")
    Port=1234
    
    ip_add=(ip,Port)

    while True:
 

        mssg=input("Enter message: ")

        message=mssg.encode("ascii")

        s.sendto(message,ip_add)
        #df=input("Do you want to send again to same address?: ")
        if mssg=="?-":
            break


while True:
    x=input("Do you want to send message: ")
    if x=="Y" or x=="y" or x=="Yes" or x=="yes":
        send()
    elif x=="N" or x=="n" or x=="No" or x=="no":
        pass
    elif x=="Q" or x=="q":
        break     


    