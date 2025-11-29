
import socket
def main():
    # connect to the server
    server_host = "127.0.0.1"
    server_port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    print("Connected to server.")
    print("Enter command (Upper/Lower/Reverse/Count/Vowels/Time/Date/Quit):")

    while True:
        # read user input

        user_input = input("enter command: ")


        # send input to server
        client_socket.send(user_input.encode())


        #if quit then close client

        if user_input.strip().upper() == "QUIT":
            print("Connection closed.")
            break


        # receive server response

        response = client_socket.recv(1024).decode()
        print("response from server:", response)

    client_socket.close()


if __name__ == "__main__":
    main()
