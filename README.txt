[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/v/release/albertphu07/Aternos-Discord-Bot?logo=github)](https://github.com/albertphu07/Aternos-Discord-Bot/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/albertphu07/Aternos-Discord-Bot/blob/main/LICENSE)

# Discord Aternos Server Bot

A Discord bot that allows users to remotely start, stop, and restart your Aternos Minecraft server directly from Discord. Built with Python using `discord.py` and `python_aternos`.

![Bot Demo](https://user-images.githubusercontent.com/yourusername/placeholder.png)

---

## Features

* Start your Minecraft server from Discord (`!start`)
* Stop your Minecraft server (`!stop`)
* Restart your Minecraft server (`!restart`)
* Prevents uncontrolled messages like "start the server"
* Logs all bot activity to `discord.log`

---

## Requirements

| Requirement       | Version / Notes               |
| ----------------- | ----------------------------- |
| Python            | 3.11+                         |
| Discord bot token | Create via Discord Dev Portal |
| Aternos account   | Username & password           |
| Python libraries  | See `requirements.txt`        |

---

## Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/albertphu07/Aternos-Discord-Bot.git
cd Aternos-Discord-Bot
```

2. **Create a `.env` file** in the root directory:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Configure the bot script**:

* Replace `YOUR_ATERNOS_USER` and `YOUR_ATERNOS_PASSWORD` with your Aternos credentials
* Replace `nodexserver1` with your Aternos server variable reference

---

## Commands

| Command    | Description                                     |
| ---------- | ----------------------------------------------- |
| `!start`   | Starts the Minecraft server (mentions everyone) |
| `!stop`    | Stops the Minecraft server                      |
| `!restart` | Restarts the Minecraft server                   |

> Messages like "start the server" are automatically deleted, guiding users to use the proper command.

---

## Logging

All bot activity and errors are logged to `discord.log`.

---

## Usage

Run the bot:

```bash
python bot.py
```

Once online, users can control the server using the commands above.

---

## Notes

* Ensure your Discord bot has **Manage Messages** and **Send Messages** permissions
* Bot intents are set to read messages and members; adjust for additional features
* Commands are case-insensitive and use the `!` prefix
* The bot currently only allows server start commands on **weekends**

---

## Example `requirements.txt`

```text
discord.py
python-dotenv
python_aternos
```

---

## License

MIT License © 2026 Nodex

---

## Optional Badges / Info

![Server Status](https://img.shields.io/badge/server-weekend%20only-yellow)
![Discord]([https://img.shields.io/discord/your-server-id?label](https://img.shields.io/discord/your-server-id?label)
