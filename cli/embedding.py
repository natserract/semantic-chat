from langchain.vectorstores import SupabaseVectorStore
from langchain_core.documents import Document
from extensions.storage.supabase_storage import SupabaseStorage
from langchain.embeddings import SpacyEmbeddings

embedder = SpacyEmbeddings(model_name="en_core_web_sm")

class Embedding:
  def __init__(self) -> None:
    pass

  def embed_documents(self, documents: list[Document], embed=True):
    supabase = SupabaseStorage()

    if embed:
      vector_store = SupabaseVectorStore.from_documents(
        documents,
        embedding=embedder,
        client=supabase.client,
        table_name="documents",
        query_name="match_documents",
        chunk_size=500,
      )

      return vector_store
    else:
      vector_store = SupabaseVectorStore(
        embedding=embedder,
        client=supabase.client,
        table_name="documents",
        query_name="match_documents",
      )
    
      return vector_store

