# ✨ UltraUserBot - Pyrogram Based Telegram UserBot 🔥

![UltraUserBot](https://i.imgur.com/G1mQF9O.png)

<p align="center">
  <b>The Ultimate Modular Telegram UserBot built with Pyrogram 💬</b><br>
  <i>Fast, lightweight, customizable, and deployable anywhere!</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/your-username/ultra-userbot?style=flat-square" />
  <img src="https://img.shields.io/github/forks/your-username/ultra-userbot?style=flat-square" />
  <img src="https://img.shields.io/github/license/your-username/ultra-userbot?style=flat-square" />
  <img src="https://img.shields.io/github/languages/top/your-username/ultra-userbot?style=flat-square" />
</p>

---

## 🔥 Features at a Glance

- 🔐 PM Permit with auto-approve
- 💌 Shayari Generator (Hindi love lines)
- 💘 Love Raid Spammer
- ✨ Magic & Emoji Animations
- 🧠 Fake Hacking Simulator
- 🖼️ Carbon Image Generator
- 😴 AFK with detection
- 😂 Laughing Animation
- 💣 Spam Commands (for fun)
- 🤬 Gali Raid (be respectful!)
- 🛠 Help system with `/help`
- 📶 Ping and uptime with `/ping`
- ✅ Alive check with bot name

---

## 💻 Deployment Options

### 🧪 Deploy to Render

> Works directly from GitHub repo!

- Fork this repo
- Go to [Render](https://render.com)
- Create new web service
- Add build & start command:

```bash
Build: pip install -r requirements.txt
Start: python3 main.py
```

- Set environment variables from `.env` (API_ID, API_HASH, SESSION, etc.)

---

### 📲 Deploy on Termux / VPS

```bash
pkg install git python -y
git clone https://github.com/<your-username>/ultra-userbot.git
cd ultra-userbot
pip install -r requirements.txt
cp .env.example .env
nano .env
python3 main.py
```

---

## 📂 Project Structure

```
ultra_userbot/
│
├── main.py                  # Entry point
├── requirements.txt         # All required packages
├── .env.example             # Sample config
├── README.md                # This file
│
├── config/
│   ├── env_config.py        # Environment loader
│   └── constants.py         # Constants
│
├── core/
│   ├── client.py            # Pyrogram client init
│   ├── loader.py            # Module loader
│   └── utils.py             # Helper functions
│
└── modules/
    ├── pmpermit.py
    ├── shayari.py
    ├── love_raid.py
    ├── magic.py
    ├── fake_hack.py
    ├── carbon.py
    ├── afk.py
    ├── laugh.py
    ├── spam.py
    ├── gali_raid.py
    ├── help.py
    ├── ping.py
    └── alive.py
```

---

## ⚙️ Environment Variables (`.env`)

```
API_ID=123456
API_HASH=your_api_hash
SESSION=your_string_session
BOT_NAME=UltraUserBot
```

> You can generate string session using [@StringSessionGenBot](https://t.me/StringSessionGenBot)

---

## 🙌 Special Thanks

- Pyrogram Library
- All Devs & Friends who helped in building this

---

## 💬 Connect

> Have an idea, feature request, or want to collab?

- Telegram: [@YourUsername](https://t.me/YourUsername)
- GitHub: [@your-username](https://github.com/your-username)

---

**Made with ❤️ for the Telegram community!**

