from dataclasses import dataclass


@dataclass
class Document:
    """
    A class representing a document.
    With its content, source, file type, and optional page number.
    """
    content: str
    source: str
    file_type: str
    page: int | None = None


@dataclass
class Chunk:
    contetn: str
    source: str
    file_type: str

    chunk_id: int

    section: str | None = None

    page_start: int | None = None
    page_end: int | None = None
