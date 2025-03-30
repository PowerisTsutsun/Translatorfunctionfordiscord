import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix="!")

# Create an instance of the Translator
translator = Translator()

@bot.command()
async def translate(ctx, target_lang: str, *, text: str):
    """
    Translates the given text into the specified target language.
    Usage: !translate <language_code> <text>
    Example: !translate es Hello, how are you?
    """
    # Check if the target language code is valid
    if target_lang.lower() not in LANGUAGES:
        valid_codes = ', '.join(sorted(LANGUAGES.keys()))
        await ctx.send(f"Invalid language code. Please use one of the following: {valid_codes}")
        return

    try:
        # Perform the translation
        result = translator.translate(text, dest=target_lang)
        # Send the translated text back to the channel
        await ctx.send(f"**Original:** {text}\n**Translated ({LANGUAGES[target_lang.lower()]}):** {result.text}")
    except Exception as e:
        await ctx.send(f"An error occurred while translating: {e}")

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
bot.run("YOUR_BOT_TOKEN")
