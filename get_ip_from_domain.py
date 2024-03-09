import socket

domainName = input("Enter the domain name: ")
ip = socket.gethostbyname(domainName)
print('IP address: ', ip)
