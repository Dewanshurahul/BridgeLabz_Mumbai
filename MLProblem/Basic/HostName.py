import socket
class Host:
    def name(self):
        return socket.gethostname()

    def ipAddress(self):
        return socket.gethostbyname(socket.gethostname())

h = Host()
print(h.name())
print(h.ipAddress())