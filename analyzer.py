from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")
toxicity_model = pipeline("text-classification", model="unitary/toxic-bert", top_k=None)

def analyze_comment(comment):
    sentiment = sentiment_model(comment)[0]
    toxicity = toxicity_model(comment)[0]

    toxic_labels = [label for label in toxicity if label['score'] > 0.5]
    is_toxic = any(label['label'] == 'toxic' for label in toxic_labels)

    return {
        "comment": comment,
        "sentiment": sentiment["label"],
        "sentiment_score": sentiment["score"],
        "toxic": is_toxic,
    }
