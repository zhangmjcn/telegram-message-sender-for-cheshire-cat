import asyncio
import urllib.parse
from typing import List

import aiohttp
from aiohttp_socks import ProxyConnector
from cat.mad_hatter.decorators import tool, hook



@tool(
    return_direct=False,
    examples=[
        "send messages to telegram",
        "inform telegram receipients",
        "发TG消息",
        "向Telegram发消息",
        "发消息到TG："
    ]
)
def send_tg_message(tool_input, cat):
    """
    This function takes a message, a sender ID and a list of chat IDs as input, sends the message to each of the provided chat IDs
    from the sender ID and returns the results of these operations.

    """
    message = tool_input['message'] if isinstance(tool_input, dict) else eval(tool_input)['message']
    send_results = "".join(asyncio.run(_send_message(message, cat)))
    print(f"send_tg_message/Results: {send_results}")
    return send_results


async def _send_message(message, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    print(f"settings: {settings}")

    sender_id = f"""bot{settings["sender_id"]}"""
    chat_ids = settings["chat_ids"]
    socks5_proxy = settings["socks5_proxy"]

    if isinstance(chat_ids, str):
        chat_ids = eval(chat_ids)

    url = f"""{settings['telegram_server_url']}/{sender_id}/sendMessage"""


    print(f"Variables: {message}, {sender_id}, {chat_ids}, {socks5_proxy}, {url}")
    # create a list of tasks
    tasks = [_send_to_target(message, sender_id, chat_id, url, socks5_proxy) for chat_id in chat_ids]

    # run all tasks concurrently
    return await asyncio.gather(*tasks)



async def _send_to_target(message: str, sender_id: str, chat_id: str, url: str, socks5_proxy: str):
    # create data for x-www-form-urlencoded
    data = urllib.parse.urlencode({
        'text': message,
        'chat_id': chat_id,
    })

    print(f"Sending message {data}")

    try:
        connector = ProxyConnector.from_url(socks5_proxy) if socks5_proxy else None
        # using application/x-www-form-urlencoded
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.post(url, data=data,
                                    headers={"Content-Type": "application/x-www-form-urlencoded"}) as resp:
                print(f"Message sent from {sender_id} to {chat_id}, status {resp.status}")
                result = await resp.text()
                return result
    except Exception as e:
        return f"未成功发送:{str(e)}"
