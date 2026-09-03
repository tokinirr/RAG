import re


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r" *\n *", "\n", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def split_paragraphs(text: str) -> list[str]:
    pargraphs: list[str] = re.split(r"\n\s*\n", text)

    return [
        paragraph.strip()
        for paragraph in pargraphs
        if paragraph.strip()
    ]


def split_sentences(text: str) -> list[str]:
    sentences: list[str] = re.split(r"(?<=[.!?])\s+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def estimate_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3)
