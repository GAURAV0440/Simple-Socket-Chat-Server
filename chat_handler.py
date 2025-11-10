import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

clients = {}

def broadcast(message, exclude_user=None):
    for user, conn in clients.items():
        if user != exclude_user:
            try:
                conn.sendall(message.encode("utf-8"))
            except:
                pass

def handle_client(conn, addr):
    username = None
    conn.sendall(b"Please login using: LOGIN <username>\n")

    while True:
        try:
            data = conn.recv(1024).decode("utf-8").strip()
            if not data:
                break

            # Split command and make case-insensitive
            parts = data.strip().split(" ", 2)
            command = parts[0].upper()

            # LOGIN flow
            if command == "LOGIN" and len(parts) > 1:
                username_candidate = parts[1].strip()
                if username_candidate in clients:
                    conn.sendall(b"ERR username-taken\n")
                else:
                    username = username_candidate
                    clients[username] = conn
                    conn.sendall(b"OK\n")
                    broadcast(f"INFO {username} joined the chat\n", exclude_user=username)

            # Messaging
            elif command == "MSG" and len(parts) > 1 and username:
                msg_text = parts[1].strip()
                broadcast(f"MSG {username} {msg_text}\n", exclude_user=None)

            # List active users
            elif command == "WHO" and username:
                for user in clients.keys():
                    conn.sendall(f"USER {user}\n".encode("utf-8"))

            # Private message
            elif command == "DM" and len(parts) > 2 and username:
                target, text = parts[1], parts[2]
                if target in clients:
                    clients[target].sendall(f"DM {username} {text}\n".encode("utf-8"))
                else:
                    conn.sendall(b"ERR user-not-found\n")

            else:
                conn.sendall(b"ERR invalid-command\n")

        except ConnectionResetError:
            break

    if username:
        del clients[username]
        broadcast(f"INFO {username} disconnected\n", exclude_user=username)
    conn.close()