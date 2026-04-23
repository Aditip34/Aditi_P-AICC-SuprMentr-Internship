
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "machine learning is fun",
    "python is great for machine learning",
    "data science uses machine learning",
    "deep learning is a part of machine learning",
    "python and data science go together"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

features = vectorizer.get_feature_names_out()

for i, doc in enumerate(X.toarray()):
    print(f"\nDocument {i+1}:")
    sorted_words = sorted(zip(features, doc), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print(word, round(score, 2))