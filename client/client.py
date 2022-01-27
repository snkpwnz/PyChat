import socket
import threading


class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                host = '192.168.56.1'
                port = 5555
                self.sock.connect((host, port))
                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.sock.send(self.username.encode())

        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler, args=())
        input_handler.start()

    def handle_messages(self):
        while 1:
            print(self.sock.recv(1204).decode())

    def input_handler(self):
        while 1:
            self.sock.send((self.username + ' - ' + input('')).encode())


client = Client()
