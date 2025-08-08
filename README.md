# WebChat

A simple yet modern real-time LAN chat application with a Flask backend and a web frontend using Socket.IO.

## Features

- Real-time chat with multiple users
- User presence display (online users list)
- Typing indicators ("user is typing...")
- Simple chat commands like `!ping` (measures latency) and `!time` (shows local time)
- Basic bot integration to respond to commands
- Stylish UI built with Tailwind CSS and custom design
- Username and user color passed via URL parameters
- Browser notifications for new messages
- Custom emoji picker with a large selection of emojis
- User avatars loaded dynamically from API
- Backend powered by Flask and Flask-SocketIO

## Recent Improvements

- **Code refactoring:** Main application logic split into smaller, well-organized modules using Flask Blueprints for routes (`routes/pages.py`, `routes/api.py`) and socket events (`sockets/events.py`), improving maintainability and readability.
- **Expanded API endpoints:** Added `/api/about`, `/api/stats/`, and `/api/bot_commands` to expose more application information and stats.
- **Enhanced frontend:** Fixed avatar color synchronization, improved sidebar info display, and disabled autocompletion to improve UX.
- **Notifications & emojis:** Implemented browser notifications for new chat messages and integrated a custom emoji popup for richer messaging experience.
- **Improved bot commands:** Better handling of commands like `!time` and `!img` for more reliable responses.
- **Folder structure reorganization:** Clear separation of concerns with dedicated folders for routes, models (including global state), sockets, and templates.

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
- Usernames and colors can be customized via URL query parameters.
- Typing notifications keep everyone aware when someone is composing a message.
- The frontend is a single-page app leveraging Socket.IO for real-time communication.

## Tech Stack

- Python with Flask & Flask-SocketIO
- HTML + Tailwind CSS for styling
- JavaScript with Socket.IO on the frontend

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Happy chatting! 🚀
