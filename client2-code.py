import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.2", 7777))

    print("Enter your account ID:")
    account_id = input()
    client_socket.sendall(account_id.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    while True:
        print("\nChoose an option:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input()
        client_socket.sendall(choice.encode())

        if choice == "1":
            balance = client_socket.recv(1024).decode()
            print(balance)
        elif choice == "2":
            print("Enter the amount to deposit:")
            amount = int(input())
            client_socket.sendall(str(amount).encode())
            response = client_socket.recv(1024).decode()
            print(response)
        elif choice == "3":
            print("Enter the amount to withdraw:")
            amount = int(input())
            client_socket.sendall(str(amount).encode())
            response = client_socket.recv(1024).decode()
            print(response)
        elif choice == "4":
            response = client_socket.recv(1024).decode()
            print(response)
            break
        else:
            response = client_socket.recv(1024).decode()
            print(response)

    client_socket.close()

if __name__ == "__main__":
    main()