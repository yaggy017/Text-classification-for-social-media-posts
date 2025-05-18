from transformers import pipeline

# Load zero-shot-classification pipeline — No training required
classifier = pipeline("zero-shot-classification")

# Expanded candidate labels — covers a wide range of common social media topics
candidate_labels = [
    "sports", "politics", "technology", "entertainment", "health", "business", "travel",
    "education", "food", "fashion", "relationships", "finance", "science", "gaming",
    "environment", "automobile", "real estate", "history", "art", "music", "memes",
    "personal updates", "career", "fitness", "books", "religion", "parenting", "news"
]

print("🚀 Social Media Post Topic Classifier 🚀")
print("Type 'exit' to quit.\n")

while True:
    post = input("Enter social media post: ")
    if post.lower() == 'exit':
        break

    # Perform zero-shot classification
    result = classifier(post, candidate_labels)

    # Show top predicted label with confidence
    top_label = result['labels'][0]
    top_score = result['scores'][0]
    print(f"🏷️ Predicted Topic: {top_label} (confidence: {top_score:.2f})\n")
