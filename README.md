# Chat Web

A simple yet modern real-time LAN chat application with a Flask backend and a web frontend using Socket.IO.

## Features

- Real-time chat with multiple users
- User presence display (online users list)
- Typing indicators ("user is typing...")
- Simple chat commands like `!ping` (measures latency) and `!time` (shows local time)
- Basic bot integration to respond to commands
- Stylish UI built with Tailwind CSS and custom design
- Username and user color passed via URL parameters
- Backend powered by Flask and Flask-SocketIO

## Live Demo

Try it out right now on [https://chat-web-o1z1.onrender.com/](https://chat-web-o1z1.onrender.com/) — no registration needed!

## How to Use

1. Clone this repo
2. Install dependencies (`pip install -r requirements.txt`)
3. Run the Flask server (`python app.py`)
4. Open your browser at `http://localhost:5000/`
5. Start chatting!

## Notes

- The chat supports a simple bot that responds to some commands (e.g., `!ping`, `!time`, `!info`).
- The frontend is (kinda) a single HTML page leveraging Socket.IO for communication.
- Usernames and colors can be customized via URL query parameters.
- Typing notifications keep everyone aware when someone is composing a message.

## Tech Stack

- Python with Flask & Flask-SocketIO
- HTML + Tailwind CSS for styling
- JavaScript with Socket.IO on the frontend

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Happy chatting! 🚀
