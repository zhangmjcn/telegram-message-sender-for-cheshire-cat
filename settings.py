# setting
from enum import Enum
from typing import Union, List, Annotated

from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, Field, BeforeValidator


def split_string(v: Union[str, List[str]]) -> List[str]:
    """Convert comma-separated string to list if needed"""

    if v is None:
        return []

    if isinstance(v, str):
        if not v.strip():  # Empty string
            return []
        return [x.strip() for x in v.split(',') if x.strip()]

    if isinstance(v, list):
        return v

    raise ValueError("limited_plugins must be a list")


class Settings(BaseModel):
    telegram_server_url: str = "https://api.telegram.org"

    sender_id: str = ""

    chat_ids: Annotated[List[str], BeforeValidator(split_string)] = []

    socks5_proxy:str = ""


@plugin
def settings_schema():
    return Settings.schema()
