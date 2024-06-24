from extractor.extractor_processor import ExtractorProcessor
from helpers.file import get_base_path
from embedding import Embedding
from langchain_fireworks import ChatFireworks
from config import Config

def run_workflow(query: str):
    # Find, extract dataset first
    extractor = ExtractorProcessor()
    markdown_path = get_base_path('datasets/archive.md')
    markdown_documents = extractor.extract(file_path=markdown_path)

    # Embed to the DB
    embeddings = Embedding()
    vector_store = embeddings.embed_documents(markdown_documents, embed=False)

    # Find similarity
    matched_docs = vector_store.similarity_search_with_relevance_scores(query)
    doc, _ = matched_docs[0]

    # Prepare the response
    messages = [
        {
            "role": "system",
            "content":"You are a NatserractAI, friendly and helpful AI assistant by Natserract that provides help with documents.",
        },
        {
            "role": "user",
            "content": query,
        },
        {
            "role": "assistant",
            "content": doc.page_content,
        },
    ]
    chat = ChatFireworks(
        model="accounts/fireworks/models/mixtral-8x7b-instruct",
        api_key=Config.FIREWORKS_API_KEY
    )
    chat.invoke(messages).pretty_print()

if __name__ == "__main__":
    query = input('\n Question: ')
    run_workflow(query)