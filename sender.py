import socket
import datetime
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_ip =  "127.0.0.1"
# target_ip = "192.168.149.51"
target_port = 63500
target_address = (target_ip,target_port)

condition = True
while condition:
  message = input("plz enter your message :")
  message_encrypted = message.encode('ascii')
  s.sendto(message_encrypted,target_address)
  print("your message is sent...")
  permission = input("")

  if permission == "Y" or permission=="y":
    condition = False