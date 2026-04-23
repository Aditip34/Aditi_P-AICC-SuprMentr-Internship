
from textblob import TextBlob

reviews = [
    "The movie was amazing and wonderful",
    "I hated the film, it was boring",
    "It was okay, not great but not bad",
    "Fantastic acting and story",
    "Worst movie ever"
]

for r in reviews:
    polarity = TextBlob(r).sentiment.polarity
    
    if polarity > 0:
        result = "Positive"
    elif polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    
    print(f"{r} → {result}")