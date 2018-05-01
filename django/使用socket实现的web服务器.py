import socket

def handle_request(client):
    data = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("<h1>Hello word</h1>")

def main():
    sockobj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockobj.bind(('localhost',8888))
    sockobj.listen(5)

    while True:
        con1,address = sockobj.accept()
        handle_request(con1)
        con1.close()

if __name__ == "__main__":
    main()