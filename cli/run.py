from extractor.extractor_processor import ExtractorProcessor
from helpers.file import get_base_path
from embedding import Embedding
from langchain_fireworks import ChatFireworks
from config import Config
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

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
    delimiter = '\n'
    context = delimiter.join([
        document.page_content for document, _ in matched_docs]
    )

    # Prepare the response
    llm = ChatFireworks(
        model="accounts/fireworks/models/mixtral-8x7b-instruct",
        api_key=Config.FIREWORKS_API_KEY,
        temperature=0.7
    )

    template = """Use the given context to answer the question.
    If you don't know the answer, say you don't know.
    Use three sentence maximum and keep the answer concise.
    Context: {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    response = qa_chain.invoke(
        context=context,
        question=query,
        input=query
    )
    print('\n Answer: ', response['result'])

if __name__ == "__main__":
    query = input('\n Question: ')
    run_workflow(query)