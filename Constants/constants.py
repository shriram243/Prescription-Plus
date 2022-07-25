import os
from pathlib import Path

PHONE_NO_REGEX : str= r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?\d{10}$"
URL_REGEX: str = "((http|https)://)(www.)?" \
            + "[a-zA-Z0-9@:%._\\+~#?&//=]" \
            + "{2,256}\\.[a-z]" \
            + "{2,6}\\b([-a-zA-Z0-9@:%" \
            + "._\\+~#?&//=]*)"
