import socketio
from server_config import connect_config
from _thread import *

server = connect_config()

def print_join_msg(user_nick):
    print('\033[46m', end = "")
    print(user_nick, end = "")
    print('\033[0m')

def print_user_msg(data):
    sender_nick, sended_msg = data['sender_nick'], data['sended_msg']
    print('{}: {}'.format(sender_nick, sended_msg))

def recv_msg(client_socket):
    while True:
        client_socket.on('msg', print_join_msg)

def send_msg(client_socket, nick):
    while True:
        msg = input(">> ")
        if msg:
            break
    client_socket.emit('msg', msg)

if __name__ == "__main__":
    client_socket = socketio.Client()
    client_socket.connect('http://163.180.118.158:8505')

    while True:
        nick = input("닉네임을 입력해주세요>> ")
        if nick:
            break
    client_socket.emit('new_user', nick)

    start_new_thread(recv_msg, (client_socket,))

    while True:
        send_msg(client_socket, nick)