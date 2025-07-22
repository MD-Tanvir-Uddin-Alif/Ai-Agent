from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def build_vector_store(chunks):
    embedding_models = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embedding_models)
    return vector_store

def query_vector_store(vector_store, query, k=3):
    docs = vector_store.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in docs])