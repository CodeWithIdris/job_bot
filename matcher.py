from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def filter_jobs(jobs, skills):

    descriptions = [job.get("description", "") for job in jobs]

    if not descriptions:
        return []

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(descriptions + [skills])

    scores = cosine_similarity(tfidf[-1], tfidf[:-1])[0]

    qualified = []

    research_keywords = [
        "research",
        "analysis",
        "analyst",
        "strategy",
        "consulting",
        "evaluation",
        "policy",
        "report",
        "data",
        "insight"
    ]

    for i, score in enumerate(scores):

        text = descriptions[i].lower()

        keyword_match = any(keyword in text for keyword in research_keywords)

        # Hybrid condition
        if score > 0.03 or keyword_match:
            qualified.append(jobs[i])

    return qualified
