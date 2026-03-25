import string

stopwords = ["is","a","the","and","in","on","at","to"]

def clean(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    words = [w for w in words if w not in stopwords]
    
    return " ".join(words)

print(clean("This is a SAMPLE text, with punctuation!"))