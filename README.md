# Discord Translator Bot

A simple Discord bot that translates text using the unofficial `googletrans` library. This bot listens for the `!translate` command and translates the given text into a specified target language.

## Features

- **Translation Command:**  
  Use the command `!translate <language_code> <text>` to translate text.
- **Language Code Validation:**  
  Validates the provided language code against supported languages.
- **Easy Setup:**  
  A minimal setup designed for quick deployment and testing.

## Prerequisites

- Python 3.9 or higher
- A Discord Bot Token (obtainable from the [Discord Developer Portal](https://discord.com/developers/applications))
- Internet connection for translation and Discord API access

## Installation

1. **Clone or Download the Repository**  
   Download the project files to your local machine.

2. **(Optional) Create a Virtual Environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate

Install Dependencies
Create a file named requirements.txt with the following content:


discord.py
googletrans==4.0.0-rc1
Then install the dependencies:


pip install -r requirements.txt
Configuration
Open the translator.py file.

Replace "YOUR_BOT_TOKEN" with your actual Discord bot token in the code:


bot.run("YOUR_BOT_TOKEN")
(Optional) For better security, consider storing your token in an environment variable and using a package like python-dotenv.

Usage
Run the Bot
Execute the following command in your terminal:


python translator.py
Use the Translation Command in Discord
In any channel where the bot has access, type:


!translate <language_code> <text>
Example:

!translate es Hello, how are you?
The bot will reply with the original text and its Spanish translation.

Troubleshooting
Ensure that your Discord bot token is correct.

Make sure the dependencies are installed properly.

Check that the bot has permissions to read and send messages in the desired channel.

License
This project is licensed under the MIT License.
