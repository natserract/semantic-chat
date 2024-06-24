from langchain_core.documents import Document
from helpers.file import get_base_path
from extractor.markdown_extractor import MarkdownExtractor

class ExtractorProcessor:
  @classmethod
  def extract(cls, file_path: str) -> list[Document]:
    extractor = MarkdownExtractor(file_path)
    return extractor.extract()