from aiogram.client.default import DefaultBotProperties
from src.configuration.logger_config import logging
from src.constants.env_constant import env_var
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import (
    Dispatcher,
    Bot
)
import requests
import json


# Initialize Bot instance with default bot properties which will be passed to all API calls
# Bot token can be obtained via https://t.me/BotFather
bot = Bot(
    token=env_var['TELEGRAM_BOT_TOKEN'],
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# All handlers should be attached to the Router (or Dispatcher)
dispatcher = Dispatcher()


class Reference:

    def __init__(self) -> None:
        self.response = ""

reference = Reference()

def clear_past():
    """A function to clear the previous conversation and context.
    """
    reference.response = ""

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer("Hi\nI am a Chat Bot! Created by Abhishek Negi. How can i assist you?")

@dispatcher.message()
async def chatgpt(message: Message)-> None:
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    logging.info(f">>> USER: \n\t{message.text}")

    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
        "model": env_var["OPENAI_MODEL"],
        "messages": [
            {"role": "assistant", "content": reference.response},  # role assistant
            {"role": "user", "content": message.text}  # our query
        ]
    })

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {env_var['OPENAI_API_KEY']}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        logging.error(f"Error: {response.status_code} - {response.text}")
        await bot.send_message(chat_id=message.chat.id, text=f"An error occurred while processing your request. {response.text}")

    resp = response.json()["choices"][0]["message"]["content"]
    print(f">>> chatGPT: \n\t{resp}")

    await bot.send_message(chat_id=message.chat.id, text=resp)


async def main() -> None:
    logging.info("Chat bot is running...")

    # And the run events dispatching
    await dispatcher.start_polling(bot)
