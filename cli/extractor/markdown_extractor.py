import re
from typing import Optional, cast
from langchain_core.documents import Document

from extractor.extractor_base import BaseExtractor

class MarkdownExtractor(BaseExtractor):
  def __init__(
      self,
      file_path: str,
      remove_hyperlinks: bool = True,
      remove_images: bool = True,
      encoding: Optional[str] = None,
  ):
    """Initialize with file path."""
    self._file_path = file_path
    self._remove_hyperlinks = remove_hyperlinks
    self._remove_images = remove_images
    self._encoding = encoding

  def extract(self) -> list[Document]:
      """Load from file path."""
      tups = self.parse_tups(self._file_path)
      documents = []
      for header, value in tups:
          value = value.strip()
          if header is None:
              documents.append(Document(page_content=value))
          else:
              documents.append(Document(page_content=f"\n\n{header}\n{value}"))

      return documents
  
  def markdown_to_tups(self, markdown_text: str) -> list[tuple[Optional[str], str]]:
      """Convert a markdown file to a dictionary.

      The keys are the headers and the values are the text under each header.

      """
      markdown_tups: list[tuple[Optional[str], str]] = []
      lines = markdown_text.split("\n")

      current_header = None
      current_text = ""

      for line in lines:
          header_match = re.match(r"^#+\s", line)
          if header_match:
              if current_header is not None:
                  markdown_tups.append((current_header, current_text))

              current_header = line
              current_text = ""
          else:
              current_text += line + "\n"
      markdown_tups.append((current_header, current_text))

      if current_header is not None:
          # pass linting, assert keys are defined
          markdown_tups = [
              (re.sub(r"#", "", cast(str, key)).strip(), re.sub(r"<.*?>", "", value))
              for key, value in markdown_tups
          ]
      else:
          markdown_tups = [
              (key, re.sub("\n", "", value)) for key, value in markdown_tups
          ]

      return markdown_tups
  
  def parse_tups(self, filepath: str) -> list[tuple[Optional[str], str]]:
      """Parse file into tuples."""
      content = ""
      try:
          with open(filepath, encoding=self._encoding) as f:
              content = f.read()
      except UnicodeDecodeError as e:
              raise RuntimeError(f"Error loading {filepath}") from e
      except Exception as e:
          raise RuntimeError(f"Error loading {filepath}") from e
      
      if self._remove_hyperlinks:
          content = self.remove_hyperlinks(content)

      if self._remove_images:
          content = self.remove_images(content)

      return self.markdown_to_tups(content)
  
  def remove_images(self, content: str) -> str:
    """Get a dictionary of a markdown file from its path."""
    pattern = r"!{1}\[\[(.*)\]\]"
    content = re.sub(pattern, "", content)
    return content

  def remove_hyperlinks(self, content: str) -> str:
    """Get a dictionary of a markdown file from its path."""
    pattern = r"\[(.*?)\]\((.*?)\)"
    content = re.sub(pattern, r"\1", content)
    return content
