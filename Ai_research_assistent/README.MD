# 🧠 AI Research Assistant (Multi-Agent System)

This project is an AI-powered **multi-agent research assistant** designed to make reading and understanding research papers easier and more efficient. It allows you to upload a PDF paper, and a set of AI agents will:

- ✅ Read and chunk the paper  
- 📝 Summarize it into structured sections  
- 💡 Explain unfamiliar technical terms and concepts  
- 🌐 Use real-time web search to enhance understanding  

It uses **LangChain** and **Gemini 1.5 Flash (via API)** in a modular, extendable architecture inspired by **RAG (Retrieval-Augmented Generation)**.

---

## 📌 Problem Formulation

> _"When reading research papers, I often get bored or stuck when I don't understand a concept. I don’t always know what to search for or where to look. This project aims to solve that by building an AI agent that not only summarizes the paper but also explains unfamiliar concepts using real-time web data."_

---

## 🧩 Architecture Overview

The system is composed of multiple specialized agents that interact with the PDF and with each other:

### 1. 📖 ReaderAgent
- Loads and chunks the uploaded research paper.
- Uses LangChain’s `PyMuPDFLoader` to parse and split the content.

### 2. 📝 SummarizerAgent
- Summarizes the research paper using Gemini 1.5 Flash.
- The summary is structured into:
  - What is the paper about?  
  - What has been done?  
  - Which model or approach was used?  
  - How the model/method was created  
  - Important considerations  
  - Results and findings

### 3. 💡 ExplainerAgent
- Detects technical terms from the paper and explains them.
- Combines:
  - In-context understanding from the paper  
  - Real-time web search  
  - Gemini 1.5 Flash for simplification

> 💡 *The architecture is modular — new agents like `CitationAgent`, `VisualizerAgent`, or `CritiqueAgent` can easily be added in the future.*

---

## ⚙️ Installation & Setup
 pip install -r requirements.txt


### 1. Clone the Repository

```bash
git clone https://github.com/MD-Tanvir-Uddin-Alif/Ai-Agent/tree/main/Ai_research_assistent.git
cd Ai_research_assistent
