import os
import fitz
import webbrowser
import threading
from flask import Flask, request, jsonify,render_template
from sentence_transformers import SentenceTransformer
from werkzeug.utils import secure_filename
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Lazy load model - only initialize when first needed
_model = None

def get_model():
    """Lazy load the model on first use"""
    global _model
    if _model is None:
        print("Loading AI model (this may take a moment on first run)...")
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def extract_text_from_pdf(file_path):
    text=""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
           
    return text.strip()

def calculate_match_score(resume_text,job_desc):
    model = get_model()
    embeddings = model.encode([resume_text, job_desc])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    return round(similarity[0][0]*100, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files or 'job_description' not in request.form:
            return "Missing file or job description", 400
        file = request.files['resume']
        job_desc = request.form['job_description']

        if file.filename == '' or not job_desc.strip():
            return "No selected file or empty job description", 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        resume_text = extract_text_from_pdf(filepath)
        score = calculate_match_score(resume_text, job_desc)

        return render_template('page.html', score=score)
    return render_template('page.html')


# if __name__ == '__main__':
#     port = 5559
#     url = f'http://127.0.0.1:{port}'
    
#     # Open browser after a short delay to ensure server is running
#     threading.Timer(0.1, lambda: webbrowser.open(url)).start()
    
#     # Run Flask app without debug mode for exe
#     app.run(port=port, debug=False)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5559))
    app.run(host='0.0.0.0', port=port, debug=False)