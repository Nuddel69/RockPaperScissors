import socket as sock


def main():
    socket_fd = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket_fd.bind(('192.168.1.49', sock.htons(1337)))
    socket_fd.listen(5)

    print("Waiting for client...")
    client = socket_fd.accept()

    if client:
        print(f"Socket connected!\nClient_Address: {client[1][0]}\tClient_Port: {client[1][1]}\n")
    else:
        print(f"Falied to connect to client.")
        return

    while True:
        messageLen = int.from_bytes(client[0].recv(4), 'big')
        if messageLen == 0 : break
        message = client[0].recv(messageLen)
        if not message : break
        print(f"> {message.decode()}")

    socket_fd.close()

if __name__ == "__main__":
    main()
