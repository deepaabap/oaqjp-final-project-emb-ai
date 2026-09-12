"""Flask web server that exposes an emotion detection endpoint."""
# pylint: disable=import-error
from flask import Flask, render_template, request
from emotion_detector import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detection():
    """Analyze the provided text and return a formatted emotion summary."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    emotions = {k: v for k, v in response.items() if k != "dominant_emotion"}
    items = [f"'{k}': {v}" for k, v in emotions.items()]
    formatted = ", ".join(items[:-1]) + " and " + items[-1]
    return (
        f"For the given statement, the system response is {formatted}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    