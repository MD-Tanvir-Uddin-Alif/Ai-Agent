from tools.pdf_loader import load_and_chunk_pdf

class ReaderAgent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.chunks = []
    
    def run(self):
        print("[ReaderAgent] Loading and chunking PDF...")
        self.chunks = load_and_chunk_pdf(self.file_path)
        
        if self.chunks:
            print(f"[ReaderAgent] ✅ Loaded {len(self.chunks)} chunks from PDF.")
        else:
            print("[ReaderAgent] ❌ No content extracted.")
        
        return self.chunks