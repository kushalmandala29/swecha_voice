from flask import Flask, render_template, request, jsonify
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torchaudio
from model import Model

# Initialize Flask app
app = Flask(__name__)

# Route to serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/voice_to_text", methods=["POST"])
def voice_to_text():
    try:
        # Check if the request contains a file
        if "file" not in request.files:
            return jsonify({"error": "No audio file provided"}), 400
        
        # Get the uploaded file
        audio = request.files["file"]
        
        # Convert the file to a tensor using torchaudio
        speech_array, sampling_rate = torchaudio.load(audio)
        
        # Instantiate the Model and perform the translation (replace this with actual model code)
        translation = Model()  # Ensure you have the correct model initialization here
        trans = translation.translate(speech_array, sampling_rate)
        
        # Return the transcription as a JSON response
        # Return the transcription as a JSON response
        return jsonify({"text": trans})

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=8000)