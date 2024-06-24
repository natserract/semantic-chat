from langchain_core.documents import Document
from helpers.file import get_base_path
from extractor.markdown_extractor import MarkdownExtractor

class ExtractorProcessor:
  @classmethod
  def extract(cls, file_path: str, return_text: bool = False) -> list[Document]:
    delimiter = '\n'
    
    extractor = MarkdownExtractor(file_path)
    return delimiter.join([
        document.page_content for document in extractor.extract()]
    ) if return_text else extractor.extract()