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


def get_last_words(text: str, n: int) -> str:
    words: list[str] = text.split()
    if not words:
        return ""
    return " ".join(words[-n:])


def add_overlap(
    chunks: list[str],
    overlap_tokens: int
) -> list[str]:

    if not chunks:
        return []

    result: list[str] = [chunks[0]]

    overlap_words: int = max(
        1,
        int(overlap_tokens / 1.3),
    )

    for current_index in range(1, len(chunks)):
        previous_chunk: str = chunks[current_index - 1]
        overlap: str = get_last_words(
            previous_chunk,
            overlap_words,
        )

        current_chunk = chunks[current_index]

        result.append(
            f"{overlap}\n\n{current_chunk}"
        )
    return result
