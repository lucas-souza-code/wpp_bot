from urllib.parse import quote
from pathlib import Path


def Msg_loader(name):
    msg_path = Path() / "data" / "message.txt"  

    # check if message file exists ( Verifica se o arquivo de mensagem existe )
    if not msg_path.exists():
        return None

    # open and read message file ( Abre e lê o arquivo de mensagem )
    with open(msg_path, "r", encoding="utf-8") as file:
        MESSAGE = file.read()

    # replace {name} placeholder if exists ( Substitui {name} se existir )
    if "{name}" in MESSAGE:
        MESSAGE = MESSAGE.replace("{name}", name)

    # encode message for URL ( Codifica a mensagem para URL )
    ENCODED_MSG = quote(MESSAGE)

    return ENCODED_MSG
