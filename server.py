import socket
import threading
import os
from chat_handler import handle_client

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 4000))

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"✅ Server running on port {PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped manually.")