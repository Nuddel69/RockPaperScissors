import socket as sock

# \x0a = Rock
# \x0b = Paper
# \x0c = Scissors

# \x1a = Tie
# \x1b = You win
# \x1c = You lose

def main():
    score = {
        b'\x1a' : 
'''****************
*  It's a tie! *
****************''',

        b'\x1b' : 
'''****************
*   You won!   *
****************''',

        b'\x1c' : 
'''****************
*  You lost!   *
****************'''
    }

    serverAddr = ('192.168.1.49', sock.htons(1337))
    socket_fd = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    print(f"Attempting to connect to the server at {serverAddr[0]}:{sock.ntohs(serverAddr[1])}")
    try:
        socket_fd.connect(serverAddr)
    except:
        print("Failed to connect to the server.")
        socket_fd.close()
        return

    print("Let's play Rock, Paper, Scissors!\nReply to the prompt with either:\n[1] Rock\n[2] Paper\n[3] Scissors")
    prompt = True
    while prompt:
        prompt = False
        choice = input("> ")
        match choice:
            case '1':
                socket_fd.send(b'\x0a')
            case '2':
                socket_fd.send(b'\x0b')
            case '3':
                socket_fd.send(b'\x0c')
            case _:
                print("Invalid input. Please enter a number between 1 and 3 to make your choice.")
                prompt = True

    while True:
        recv = socket_fd.recv(1)
        if recv:
            print(score[recv])
            break

    socket_fd.close()

if __name__ == "__main__":
    main()
