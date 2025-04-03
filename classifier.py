from transformers import pipeline


# Load the zero-shot classifier pipeline (this will download the model if not cached)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# Define candidate labels (adjust or expand this list)
candidate_labels = ["taxes", "travel", "medical", "finance", "personal", "other"]


def categorize_text(text):
    result = classifier(text, candidate_labels=candidate_labels)
    top_label = result['labels'][0]        # e.g. "taxes" or "travel"
    score = result['scores'][0]
    print(f"Top category: {top_label} (score={score:.2f})")
    return top_label
