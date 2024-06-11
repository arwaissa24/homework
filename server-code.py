import socket
import threading

ACCOUNTS = {
    "Aya": 25000,
    "Alaa": 3000
}

def handle_client(conn, addr):
    print("New connection from {}".format(addr))
    try:
        account_id = conn.recv(1024).decode()
        if account_id not in ACCOUNTS:
            conn.sendall("Invalid account ID".encode())
            return

        balance = ACCOUNTS[account_id]
        conn.sendall("Welcome to the bank ATM! Your current balance is: {}".format(balance).encode())

        while True:
            choice = conn.recv(1024).decode()
            if choice == "1":
                conn.sendall("Your balance is: {}".format(balance).encode())
            elif choice == "2":
                amount = int(conn.recv(1024).decode())
                balance += amount
                ACCOUNTS[account_id] = balance
                conn.sendall("Deposit successful. Your new balance is: {}".format(balance).encode())
            elif choice == "3":
                amount = int(conn.recv(1024).decode())
                if amount > balance:
                    conn.sendall("Insufficient funds".encode())
                else:
                    balance -= amount
                    ACCOUNTS[account_id] = balance
                    conn.sendall("Withdrawal successful. Your new balance is: {}".format(balance).encode())
            elif choice == "4":
                conn.sendall("Thank you for using the bank ATM. Your final balance is: {}".format(balance).encode())
                break
            else:
                conn.sendall("Invalid choice".encode())

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 7777))
    server_socket.listen(5)
    print("Server is listening on localhost:7777")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
