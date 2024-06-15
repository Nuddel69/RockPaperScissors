import socket as sock

def main():
    serverAddr = ('192.168.1.49', sock.htons(1337))
    socket_fd = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    print(f"Attempting to connect to the server at {serverAddr[0]}:{sock.ntohs(serverAddr[1])}")
    try:
        socket_fd.connect(serverAddr)
    except:
        print("Failed to connect to the server.")
        socket_fd.close()
        return

    socket_fd.close()

if __name__ == "__main__":
    main()
