import telegram


class TelegramSender:
    def __init__(self, token: str, chat_id: int):
        self.bot = telegram.Bot(token)
        self.chat = chat_id
        self.send_text("start telegram bot", chat_id)

    def send_text(self, text, chat_id, parse_mode="Markdown"):
        self.bot.send_message(text=text, chat_id=chat_id, parse_mode=parse_mode)


if __name__ == '__main__':
    token = "xxxxxx"
    chat_id = 111111
    bot = TelegramSender(token, chat_id)
    bot.send_text("我们都是阴沟里的虫子，但总还是得有人仰望星空。", chat_id)
    bot.send_text("宇宙很大，生活更大，也许以后还有缘相见。", chat_id)
    bot.send_text("https://bscscan.com/address/0x72b61c6014342d914470ec7ac2975be345796c2b", chat_id)
    bot.send_text("[BNB48CLUB](https://bscscan.com/address/0x72b61c6014342d914470ec7ac2975be345796c2b)", chat_id)

