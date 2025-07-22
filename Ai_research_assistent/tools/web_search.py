from duckduckgo_search import DDGS

def web_search_tools(query, max_results=3):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            return "\n".join([r['body'] for r in results[:max_results]])
    except Exception as e:
        return f"[ERROR] Web search failed: {e}"