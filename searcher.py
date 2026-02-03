import arxiv
import json

def search_papers(keywords, max_results=5):
    results = []
    for kw in keywords:
        search = arxiv.Search(
            query=kw,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        for paper in search.results():
            results.append({
                "title": paper.title,
                "authors": [a.name for a in paper.authors],
                "summary": paper.summary,
                "pdf_url": paper.pdf_url
            })
    return results
