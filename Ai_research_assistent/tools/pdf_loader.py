# from langchain.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_pdf(file_path, chunk_size=800, chunk_overlap=150):
    try:
        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap
        )
        
        chunks = splitter.split_documents(docs)
        return chunks
    except Exception as e:
        print(f"[ERROR] Failed to load and chunk PDF: {e}")
        return[]