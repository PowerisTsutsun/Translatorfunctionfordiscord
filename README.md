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

`
pip install -r requirements.txt
Configuration
Open the translator.py file.
`

```
!translate <language_code> <text>
```
## Example:
 ```bash
- !translate es Hello, how are you?
The bot will reply with the original text and its Spanish translation.
```

## Troubleshooting
- Ensure that your Discord bot token is correct.
- Make sure the dependencies are installed properly.

`Check that the bot has permissions to read and send messages in the desired channel.`

License
This project is licensed under the MIT License.
