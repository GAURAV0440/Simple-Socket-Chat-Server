## Simple Socket Chat Server
Backend Assignment — Real-Time TCP Chat using Python

### Overview
This is a simple TCP-based chat server built only with Python’s standard socket library.
It allows multiple users to connect, log in with unique usernames and chat in real-time — directly from the terminal.


### Tech Stack
Language: Python
Libraries Used:
socket (for TCP communication)
threading (for multiple clients)
os, dotenv (for PORT configuration)

## Project Structure
<img width="353" height="311" alt="image" src="https://github.com/user-attachments/assets/db738bfc-ed20-44f5-8e14-cfa6bca24ae9" />

### Setup Instructions (Windows / Linux)
#### 1️⃣ Go to project folder
cd socket_chat_server

#### 2️⃣ Create and activate virtual environment

Linux / Mac:
python3 -m venv .venv && source .venv/bin/activate

Windows (PowerShell):
python -m venv .venv ; .\.venv\Scripts\activate

#### 3️⃣ Install dependencies (optional)
pip install -r requirements.txt

#### 4️⃣ Run the server
python server.py


### Server will start on:
✅ Server running on port 4000

### How to Connect Clients
Open two or more terminals in the same folder.
### Terminal 1 (Server)
python3 server.py

### Terminal 2 (Client 1)
nc localhost 4000
LOGIN GAURAV
MSG Hello everyone!

### Terminal 3 (Client 2)
nc localhost 4000
LOGIN BOB
MSG Hi Gaurav!

### Example Interaction:
Client 1 (GAURAV)
LOGIN GAURAV
OK
MSG Hello everyone!
MSG GAURAV Hello everyone!
INFO BOB joined the chat
MSG BOB Hi Gaurav!

Client 2 (BOB)
LOGIN BOB
OK
MSG Hi Gaurav!
MSG GAURAV Hello everyone!

If Client 1 disconnects:
INFO GAURAV disconnected

### Command	Description	Example
LOGIN <username>	Log in with a username	LOGIN Gaurav
MSG <text>	Send a public message	MSG Hello everyone!
WHO	List all active users	WHO
DM <username> <text>	Send private message	DM Bob hi!
Commands are case-insensitive — both LOGIN / login and MSG / msg work.

### Screen Recording:
You can watch the short demo (server + 2 clients chatting) here:
https://www.loom.com/share/59d12060c50c4a2591165d7b63581e6e

### Optional Features (Implemented):
1. WHO → list of active users
2. DM <username> <text> → private messaging
3. Case-insensitive command handling
4. Graceful manual shutdown with Ctrl + C


