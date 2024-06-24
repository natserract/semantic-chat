from langchain_community.vectorstores import SupabaseVectorStore
from langchain_core.documents import Document
from extensions.storage.supabase_storage import SupabaseStorage
from langchain.embeddings.openai import OpenAIEmbeddings

class Embedding:
  def __init__(self) -> None:
    pass

  def embed_documents(self, documents: list[Document]):
    supabase = SupabaseStorage()
    embeddings = OpenAIEmbeddings()

    # TODO: check if embeddings has been stored, do not retrieve again
    vector_store = SupabaseVectorStore.from_documents(
      documents,
      embeddings,
      client=supabase.client,
      table_name="documents",
      query_name="match_documents",
      chunk_size=500,
    )

    return vector_store

