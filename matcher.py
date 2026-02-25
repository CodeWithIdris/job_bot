from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def filter_jobs(jobs, skills):
    descriptions = [job.get("description", "") for job in jobs]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(descriptions + [skills])

    scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    qualified = []

    for i, score in enumerate(scores[0]):
        if score > 0.15:  # adjust threshold
            qualified.append(jobs[i])

    return qualified
    