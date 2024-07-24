reviews = ["This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(reviews, keywords):
    for review in reviews:
        highlighted_review = review
        for word in keywords:
            highlighted_review = highlighted_review.replace(word, word.upper())
        print(highlighted_review)

highlight_keywords(reviews, keywords)

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_sentiment(review, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    words = review.lower().split()
    
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    
    return positive_count, negative_count

for review in reviews:
    positive, negative = tally_sentiment(review, positive_words, negative_words)
    print(f"Review: {review}")
    print(f"Positive words: {positive}, Negative words: {negative}")
    print()

def create_summary(review, max_length=30):
    review = review[:-1]
    if len(review) <= max_length:
        return review
    
    last_space = review.find(" ", max_length)
    if last_space != -1:
        summary = review[:last_space] + "…"
    else:
        summary = review[:max_length] + "…"
    
    return summary

for review in reviews:
    summary = create_summary(review)
    print(f"Review: {review}")
    print(f"Summary: {summary}")
    print()
