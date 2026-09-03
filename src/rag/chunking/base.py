from abc import ABC, abstractmethod
from rag.models.document import Document, Chunk


class BaseChunker(ABC):
    def __init__(
        self,
        target_tokens: int = 600,
        max_tokens: int = 800,
        overlap_tokens: int = 80
    ) -> None:
        self.target_tokens: int = target_tokens
        self.max_tokens: int = max_tokens
        self.overlap_tokens: int = overlap_tokens

    @abstractmethod
    def chunk(self, document: Document) -> list[Chunk]:
        pass
