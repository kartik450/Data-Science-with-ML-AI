import socket as sk

def rece():
    s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

    ip=input("Enter ip address: ")
    port=1234
    ip_add=(ip,port)
    tp=s.bind(ip_add)
    while True:
        msg=s.recvfrom(10000)
        mssg=msg[0]
        message=mssg.decode("ascii")
        print(message)

while True:
    con=input("Do you want to start receiving?: ")
    if con=="Y" or con=="y" or con=="Yes" or con=="yes":
        rece()    
