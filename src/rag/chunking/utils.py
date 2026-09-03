import re
from typing import Any


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r" *\n *", "\n", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def split_paragraphs(text: str) -> list[str]:
    pargraphs: list[str | Any] = re.split(r"\n\s*\n", text)

    return [
        paragraph.strip()
        for paragraph in pargraphs
        if paragraph.strip()
    ]
