
import re

POSITIVE_KEYWORDS = {
    "excellent", "helpful", "clear",
    "engaging", "interesting", "supportive"
}

NEGATIVE_KEYWORDS = {
    "poor", "confusing", "boring",
    "difficult", "unhelpful", "disappointing"
}


def tokenize(sentence):
    """Extract words and normalize them to lowercase."""
    return re.findall(r"\b[a-zA-Z]+\b", sentence.lower())


def classify_sentiment(score):
    if score >= 2:
        return "Positive"
    elif score == 1:
        return "Slightly Positive"
    elif score == 0:
        return "Neutral"
    elif score == -1:
        return "Slightly Negative"
    else:
        return "Negative"


def analyse_feedback(sentence):
    words = tokenize(sentence)

    positive_matches = [
        word for word in words
        if word in POSITIVE_KEYWORDS
    ]

    negative_matches = [
        word for word in words
        if word in NEGATIVE_KEYWORDS
    ]

    positive_count = len(positive_matches)
    negative_count = len(negative_matches)
    score = positive_count - negative_count

    return {
        "feedback": sentence,
        "positive_keywords": positive_matches,
        "negative_keywords": negative_matches,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "score": score,
        "sentiment": classify_sentiment(score)
    }


def analyse_multiple_feedback(feedback_list):
    results = []

    for sentence in feedback_list:
        results.append(analyse_feedback(sentence))

    return results


feedback = [
    "The teacher is excellent and helpful.",
    "The lectures are confusing and boring.",
    "The explanation is clear and interesting.",
    "The course is difficult but engaging.",
    "The classroom is comfortable."
]

results = analyse_multiple_feedback(feedback)

for index, result in enumerate(results, start=1):
    print(f"\nFeedback {index}: {result['feedback']}")
    print("Positive matches:", result["positive_keywords"])
    print("Negative matches:", result["negative_keywords"])
    print("Positive count:", result["positive_count"])
    print("Negative count:", result["negative_count"])
    print("Score:", result["score"])
    print("Classification:", result["sentiment"])
