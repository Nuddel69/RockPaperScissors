import socket as sock

# \x0a = Rock
# \x0b = Paper
# \x0c = Scissors

# \x1a = Tie
# \x1b = You win
# \x1c = You lose

def main():

    rules = {
        b'\x0a': b'\x0c',
        b'\x0b': b'\x0a',
        b'\x0c': b'\x0b'
    }

    socket_fd = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket_fd.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
    try:
        socket_fd.bind(('192.168.1.49', sock.htons(1337)))
    except:
        print("Port in use. Closing...")
        socket_fd.close()
        return
    socket_fd.listen(5)

    print("Waiting for client...")
    player1_sock, player1_address = socket_fd.accept()
    if player1_sock:
        print(f"Player 1 connected!\nClient_Address: {player1_address[0]}\tClient_Port: {player1_address[1]}\n")
    else:
        print(f"Falied to connect to client.")
        return

    player2_sock, player2_address = socket_fd.accept()
    if player2_sock:
        print(f"Player 2 connected!\nClient_Address: {player2_address[0]}\tClient_Port: {player2_address[1]}\n")
    else:
        print(f"Falied to connect to client.")
        return

    p1_ans = player1_sock.recv(1)
    p2_ans = player2_sock.recv(1)

    if (p1_ans == p2_ans):
        print("Tie!")
        player1_sock.send(b'\x1a')
        player2_sock.send(b'\x1a')

    if rules[p1_ans] == p2_ans:
        print("Player 1 wins!")
        player1_sock.send(b'\x1b')
        player2_sock.send(b'\x1c')
    else:
        print("Player 2 wins!")
        player1_sock.send(b'\x1c')
        player2_sock.send(b'\x1b')

    socket_fd.close()

if __name__ == "__main__":
    main()
