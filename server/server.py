import socket
import threading
from server_commander import commander
from sqlite import Sqlite


class Server:
    def __init__(self):
        self.database = Sqlite()
        self.start_server()

    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = socket.gethostbyname(socket.gethostname())
        port = int(input('Enter port to run the server on --> '))

        self.clients = []

        self.sock.bind((host, port))
        self.sock.listen(100)

        print('Running on host: ' + str(host))
        print('Running on port: ' + str(port))

        self.username_lookup = {}

        while True:
            connection, addr = self.sock.accept()
            username = connection.recv(1024).decode()

            print('New connection. Username: ' + str(username))

            self.broadcast('New person joined the room. Username: ' + username)

            self.username_lookup[connection] = username

            self.clients.append(connection)

            threading.Thread(target=self.handle_client, args=(connection, addr,)).start()

    # Send message to all users
    def broadcast(self, msg):
        for connection in self.clients:
            connection.send(msg.encode())

    # Handling incoming connections
    def handle_client(self, c, addr):
        while True:
            try:
                msg = c.recv(1024)
                print(msg.decode())
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)

                print(str(self.username_lookup[c]) + ' left the room.')
                self.broadcast(str(self.username_lookup[c]) + ' has left the room.')
                break

            if msg.decode().split(' - ')[1].startswith('/'):
                for connection in self.clients:
                    if connection == c:
                        commander.command(data=msg.decode().split(' - ')[1], sock=connection)
            elif msg.decode() != '':
                content = msg.decode().split(' - ')
                self.database.add_message(content[0], content[1])
                print('New message: ' + str(msg.decode()))
                for connection in self.clients:
                    if connection != c:
                        connection.send(msg)


server = Server()
