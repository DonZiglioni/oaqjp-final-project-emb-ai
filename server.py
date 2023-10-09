""" Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector", template_folder='templates')

@app.route("/emotionDetector")
def sent_detection():
    """ This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion ratings 
        and dominant emotion for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger is None:
        return 'Invalid input!  Try again...'
    return F"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.  The dominant emotion is <b>{dominant_emotion}</b>"

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #""" This functions executes the flask app and deploys it on localhost:5000 """