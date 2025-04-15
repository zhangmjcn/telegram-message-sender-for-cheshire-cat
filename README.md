# telegram-message-sender-for-cheshire-cat
## Introduction
This plugin enables the Cheshire Cat AI platform to send messages to Telegram users or groups. It provides a simple way to integrate your Cheshire Cat instance with Telegram's messaging system, allowing the AI to notify users through Telegram when necessary.
## Features
- Send messages to multiple Telegram chat IDs simultaneously
- Support for SOCKS5 proxy for connections in restricted networks
- Configurable Telegram API server URL
- Easy setup through the Cheshire Cat plugin interface

## Installation
1. Install this plugin through the Cheshire Cat plugin store
2. Configure the plugin settings as described below

## Configuration
The plugin requires the following settings:

| Setting | Description | Default |
| --- | --- | --- |
| `telegram_server_url` | Telegram API server URL | [https://api.telegram.org](https://api.telegram.org) |
| `sender_id` | Your Telegram bot token (without "bot" prefix) | "" |
| `chat_ids` | List of Telegram chat IDs to send messages to (comma-separated) | [] |
| `socks5_proxy` | Optional SOCKS5 proxy URL | "" |
### How to get the required information:
1. **Telegram Bot Token**: Create a new bot using [BotFather](https://t.me/botfather) and copy the provided token
2. **Chat IDs**: Start a chat with your bot and use a service like [@userinfobot](https://t.me/userinfobot) to get your chat ID

## Usage
Once configured, you can use the tool in your Cheshire Cat interactions. The plugin adds a tool that can be invoked in conversations with prompts like:
- "Send messages to telegram"
- "Inform telegram recipients"
- "发TG消息"
- "向Telegram发消息"
- "发消息到TG："

### Example
``` 
User: Please send a notification to my Telegram saying "The system process has completed"
Cheshire Cat: I'll send that message to Telegram for you.
```
## Error Handling
The plugin provides error messages when:
- The connection to Telegram API fails
- The proxy settings are incorrect
- The bot token or chat IDs are invalid

## Development
This plugin is open source. Feel free to contribute by submitting pull requests or reporting issues on the repository.
## License
[GNU GENERAL PUBLIC LICENSE](./LICENSE)
## Author
Jay ZHANG (zhangmjcn@gmail.com)
