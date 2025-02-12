from flask import Flask, request, jsonify,render_template,url_for,request
import pickle
import re
# Load trained model and vectorizer
model = pickle.load(open('D:/workplace/work/model.pkl', 'rb'))
vectorizer = pickle.load(open('D:/workplace/work/vectorizer.pkl', 'rb'))
# Initialize the Flask application
app = Flask(__name__,template_folder = 'template')

def clean_text(text):
    # Lowercase the text
    text = text.lower()
    #Removing the square brackets
    text = re.sub(r'\[[^]]*\]', '', text)
    # Remove <br /> tags (if any)
    text = re.sub(r'<br\s*/?>', '', text)
    # Removing special characters
    text = re.sub('[^a-zA-Z]', ' ',text)
    text = ''.join(text)

    return text

# Define the prediction endpoint
@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    error = None
    if request.method == 'POST':
        review_text = request.form.get('review_text')
        
        if not review_text:
            error = "Review text is required"
        else:
            try:
                # Preprocess and predict sentiment as you did before
                processed_text = clean_text(review_text)
                text_vector = vectorizer.transform([processed_text])
                prediction = model.predict(text_vector)
                sentiment = "positive" if prediction == 1 else "negative"
            except Exception as e:
                error = str(e)
    
    return render_template('home.html', sentiment=sentiment, error=error)


if __name__ == '__main__':
    app.run(debug=True)

