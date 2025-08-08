# 💬 WebChat

A simple yet modern real-time LAN chat app with a Flask backend and web frontend using Socket.IO.  
Chat from your browser — no account, no cloud, just LAN.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5a131e4a-6fc9-480d-a83b-62b8cbbcda8f" alt="Chat UI" width="400"/>
  <img src="https://github.com/user-attachments/assets/aec578ac-958f-41a1-a93a-d3721a0333c6" alt="Login screen" width="400"/>
</p>

---

## 🧭 Table of Contents

- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
- [📦 Recent Improvements](#-recent-improvements)
- [🛠 Tech Stack](#-tech-stack)
- [📝 Notes](#-notes)
- [🖥 Screenshots](#-screenshots)
- [📄 License](#-license)

---

## ✨ Features

- ⚡ Real-time chat with multiple users
- 🙋 Online user list
- ⌨️ Typing indicators (`user is typing...`)
- 💬 Commands like `!ping` (latency), `!time` (local time)
- 🤖 Simple bot support
- 🎨 Tailwind CSS styled UI
- 🌈 Custom usernames & colors via URL params
- 🔔 Browser notifications
- 😃 Emoji picker with wide emoji support
- 🧑‍🎨 Dynamic avatars via external API
- 🧠 Backend: Flask + Flask-SocketIO

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/McDjXdLol/WebChat.git
cd WebChat

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```
Now open your browser at [http://localhost:5000](http://localhost:5000) and enjoy chatting 🎉

# 📦 Recent Improvements
- 📂 Code refactor: Modular structure via Flask Blueprints (routes/, sockets/, models/)
- 📡 New API endpoints: /api/about, /api/stats/, /api/bot_commands
- 🎨 Frontend polish: Avatar syncing, sidebar info, UX tweaks
- 🔔 Notifications: Browser alerts for new messages
- 😄 Emoji support: Custom emoji picker popup
- 🤖 Bot upgrades: Improved !ping, !time, !img handling
- 🗂 Better structure: Clean folder separation for routes, sockets, templates, etc.

# 🛠 Tech Stack
| Layer     | Tech                          |
| --------- | ----------------------------- |
| Backend   | Python, Flask, Flask-SocketIO |
| Frontend  | HTML, Tailwind CSS, JS        |
| Real-Time | Socket.IO                     |
| Bot/API   | Python + internal commands    |


# 📝 Notes
- 🧠 The bot responds to !ping, !time, !info, !img, etc.
- 🎨 Customize username & color via URL: ?user=Mc&color=cyan
- 💬 Typing indicators keep everyone in sync
- 🔄 Messages are updated live via WebSockets

# 🖥 Screenshots
<p align="center"> <img src="https://github.com/user-attachments/assets/5a131e4a-6fc9-480d-a83b-62b8cbbcda8f" alt="Chat UI" width="400"/> <img src="https://github.com/user-attachments/assets/aec578ac-958f-41a1-a93a-d3721a0333c6" alt="Login screen" width="400"/> </p>

# 📄 License
This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

Happy chatting! 🚀

---

Made with ❤️ and a bit of caffeine ☕
