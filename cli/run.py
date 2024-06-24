from extractor.extractor_processor import ExtractorProcessor
from helpers.file import get_base_path
from embedding import Embedding
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from config import Config

def run_workflow(query: str):
    # Find, extract dataset first
    extractor = ExtractorProcessor()
    markdown_path = get_base_path('datasets/archive.md')
    markdown_documents = extractor.extract(file_path=markdown_path)

    # Embed to the DB
    embeddings = Embedding()
    vector_store = embeddings.embed_documents(markdown_documents)

    # Find similarity
    matched_docs = vector_store.similarity_search(query)
    injected_docs = "\n\n".join([doc.page_content for doc in matched_docs])

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
            "content": injected_docs,
        },
    ]
    llm = ChatOpenAI(model=Config.OPENAI_MODEL, api_key=Config.OPENAI_API_KEY)
    print('AI Response: ', llm.invoke(messages))

if __name__ == "__main__":
    query = "Geography in Indonesia?"
    run_workflow(query)