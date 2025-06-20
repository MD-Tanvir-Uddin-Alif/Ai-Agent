# AI Deal Finder

An AI-powered multi-site deal finder that scrapes Amazon, Daraz, and eBay to find the best product deals based on user queries.  
Built using **Google Gemini LLM**, **LangChain**, and **BeautifulSoup** for scraping. Supports natural language search and aggregates top deals with prices, ratings, and direct links.

---

## Features

- Search for deals across multiple marketplaces: Amazon, Daraz, eBay  
- Aggregates and ranks deals by price  
- Handles natural language queries with or without price ranges and location  
- Interactive command-line interface for quick deal discovery  
- Easily extendable with new scraping tools or marketplaces  
- Powered by Google Gemini LLM and LangChain tool-calling agents  

---

## Getting Started

### Prerequisites

- Python 3.8+  
- Google Cloud API key with access to Gemini models  
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MD-Tanvir-Uddin-Alif/Ai-Agent/tree/main/Ai-Deal-finder
   cd Ai-Deal-finder


## Setup and Usage

### Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

