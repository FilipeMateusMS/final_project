"""
This Flask application provides an emotion detection service.
It takes text input, analyzes it for emotions using an external
emotion_detector module, and returns the detected emotions,
including a dominant emotion.
"""
import json
from flask import Flask, render_template, request

# Assuming EmotionDetection is a local module you have
from EmotionDetection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the given text and return detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze")

    # Basic input validation for empty or None text
    if not text_to_analyze:
        return "Invalid Input! Please provide text to analyze.", 400 # Added status code

    analyze_result = emotion_detector(text_to_analyze)

    # Check if emotion_detector returned a valid (non-None) result
    if analyze_result is None:
        return "Error: Could not process the text for emotion detection.", 500 # Added status code

    try:
        items = json.loads(analyze_result)
    except json.JSONDecodeError:
        return "Error: Invalid JSON response from emotion detector.", 500

    # Ensure the 'items' dictionary is not empty and contains expected keys
    if not isinstance(items, dict) or not items:
        return "Error: Unexpected response format from emotion detector.", 500

    dominant_emotion = items.pop("dominant_emotion", None)
    if dominant_emotion is None:
        return "Error: Dominant emotion not found in the response.", 500

    sentiment_parts = []
    # Sort items for consistent output, though not strictly necessary
    sorted_items = sorted(items.items())

    for i, (key, value) in enumerate(sorted_items):
        sentiment_parts.append(f"'{key}': {value}")

    # Join the sentiment parts with ", "
    response_text_parts = ", ".join(sentiment_parts)

    return (
        f"For the given statement, the system response is {response_text_parts}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001) # Use 0.0.0.0 to make it accessible externally