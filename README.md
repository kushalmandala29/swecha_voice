# Swecha Voice

Swecha Voice is a Telugu voice recognition project built around a **fine-tuned Whisper model**.

The model and application were developed **collaboratively by contributors from the Swecha AP (Swecha Andhra Pradesh) community**, who:

- Collected **Telugu language voice samples** from volunteers.
- Prepared and curated a custom dataset.
- Fine-tuned OpenAI’s Whisper model to better recognize and transcribe Telugu speech.
- Built a simple **web-based interface** to make the model easy to use.

The repository contains:

- A **web interface** (primarily HTML) for recording and sending audio.
- **Python code** for loading and running the fine-tuned Whisper model and serving predictions.

---

## Table of Contents

- [Overview](#overview)
- [Community & Collaboration](#community--collaboration)
- [Data Collection](#data-collection)
- [Model](#model)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technology Stack](#technology-stack)
- [Limitations and Future Work](#limitations-and-future-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

Swecha Voice focuses on **Telugu Automatic Speech Recognition (ASR)**:

- Targets **Telugu speech-to-text** using a fine-tuned Whisper model.
- Uses **community-collected Telugu voice data** from Swecha AP.
- Provides a **browser-based UI** for recording audio and viewing transcriptions.
- Serves as a foundation for Telugu voice interfaces, accessibility tools, and language technology research.

Typical use-cases:

- Telugu speech-to-text for notes, captions, or content creation.
- Voice interfaces for Telugu-centric applications.
- Educational and research projects around low-resource language ASR.

---

## Community & Collaboration

This project is a **community-driven effort by Swecha AP**:

- Developed by volunteers and contributors from **Swecha Andhra Pradesh**.
- Emphasizes **free software**, **local language empowerment**, and **community-owned technology**.
- Encourages contributions from students, activists, and developers interested in:
  - Telugu language technology
  - Free and open source tools
  - Ethical data collection and AI

If you are part of Swecha AP or want to collaborate, feel free to:

- Open issues and pull requests.
- Contribute code, documentation, or Telugu voice data.
- Help test and evaluate the model in real-world scenarios.

---

## Data Collection

The model is trained on **custom Telugu voice samples**:

- Collected from **Telugu speakers** in the community.
- Audio files are labeled with matching Telugu text.
- Data is cleaned and preprocessed (e.g., silence trimming, format normalization).

You can update this section with concrete details, such as:

- **Number of speakers**: `N`  
- **Total duration**: `~X hours` of Telugu speech  
- **Audio format**: `16 kHz, mono, WAV` (example)  
- **Transcription format**: plain text (`.txt`) or JSON aligned to audio files  
- Any **data consent** and **privacy** guidelines followed by Swecha AP

If there are dataset or collection guidelines, link or describe them here.

---

## Model

The ASR system is powered by a **fine-tuned Whisper model**:

- **Base model**: `whisper-base`, `whisper-small`, `whisper-medium`, etc. (update with actual).
- **Objective**: improve **Telugu speech recognition** performance over the base multilingual model.
- **Training**:
  - Uses the Swecha AP Telugu dataset.
  - May optionally combine with public Telugu datasets if available.

Typical pipeline:

1. **Preprocessing**
   - Convert audio to required sample rate (e.g., 16 kHz mono).
   - Normalize audio and clean noisy segments.
   - Align transcripts with audio.

2. **Fine-Tuning**
   - Train the Whisper model on the Swecha AP Telugu dataset.
   - Monitor metrics like Word Error Rate (WER) / Character Error Rate (CER).

3. **Inference**
   - Load the fine-tuned model in Python.
   - Expose an API endpoint or script to run transcription.

4. **Web Integration**
   - Record audio via browser.
   - Send audio to backend.
   - Display Telugu transcription in the UI.

> Add more technical details here:
> - Final model checkpoint location (local path / Hugging Face repo).
> - Evaluation metrics on test data.
> - Any domain-specific improvements (e.g., handling of Telugu numerals or names).

---

## Features

- 🎙️ **Telugu Speech-to-Text**  
  Record Telugu speech in the browser and receive automatic transcriptions.

- 🗣️ **Community-Curated Dataset**  
  Model is fine-tuned on voice samples collected by **Swecha AP** volunteers.

- 🌐 **Web-Based Interface**  
  Simple HTML interface for:
  - Starting/stopping microphone recording
  - Sending audio to backend
  - Viewing Telugu transcription

- 🧠 **Whisper-Based ASR**  
  Built on top of the Whisper architecture, adapted specifically for Telugu.

- ✊ **Free Software & Local Language Focus**  
  Aims to empower Telugu speakers with open and community-owned tools.

---

## Project Structure

> Adjust this example to reflect the actual layout of your repository.

```text
swecha_voice/
├─ index.html             # Main HTML UI
├─ static/                # CSS, JS, and other assets
│  ├─ css/
│  └─ js/
├─ app.py                 # Python backend / API for Whisper inference
├─ model/                 # Model loading utilities / weights (if stored locally)
│  └─ load_model.py
├─ data/                  # (Optional) Sample or demo Telugu audio/transcripts
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
```

---

## Getting Started

### Prerequisites

- **Python**: 3.8+  
- **pip**  
- **Git**  
- A modern web browser (with microphone access enabled).

For audio and Whisper:

- **PyTorch** (CPU or GPU version depending on your hardware).
- **ffmpeg** for audio processing.

Example installation (Debian/Ubuntu):

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Installation

Clone the repository:

```bash
git clone https://github.com/kushalmandala29/swecha_voice.git
cd swecha_voice
```

Install Python dependencies (if `requirements.txt` is present):

```bash
pip install -r requirements.txt
```

If the fine-tuned model is hosted externally (e.g., Hugging Face or a shared storage), follow the project’s instructions to download or configure the model path.

### Running the Project

> Update this section according to your actual server entry point / framework.

Example (Flask-style):

```bash
export FLASK_APP=app.py
export FLASK_ENV=development  # optional
flask run
```

or:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## Usage

1. **Open the web interface**  
   Go to the URL where the app is running (e.g., `http://127.0.0.1:5000`).

2. **Allow microphone access**  
   When the browser prompts you, allow microphone permissions.

3. **Record Telugu speech**  
   Click **Record** and speak in Telugu.

4. **Stop recording**  
   Click **Stop** or the provided control.

5. **View transcription**  
   The backend sends the audio to the fine-tuned Whisper model, and the predicted **Telugu text** is shown on the page.

6. **Copy or use the result**  
   Use the transcribed text for documentation, subtitles, notes, or further NLP processing.

> Add screenshots or demo GIFs from Swecha AP events or testing sessions if available.

---

## Configuration

If you use configuration files or environment variables, describe them here. For example:

- `.env` (if present):
  - `MODEL_PATH` – file path or identifier of the fine-tuned Whisper model.
  - `DEVICE` – `cpu` or `cuda`.
  - `HOST` / `PORT` – server host/port.
- Python config file (e.g., `config.py`) for more advanced settings.

Example:

```bash
cp .env.example .env
# Edit .env to set MODEL_PATH, DEVICE, etc.
```

---

## Technology Stack

- **Model**
  - Fine-tuned **Whisper** model for Telugu ASR

- **Backend**
  - Python (≈ 8.9% of the repository)
  - Likely stack includes:
    - `torch`
    - `openai-whisper` or `transformers`
    - A web framework like `Flask` or `FastAPI` (update as needed)

- **Frontend**
  - HTML (≈ 91.1% of the repository)
  - JavaScript for accessing the microphone and sending audio
  - Basic CSS for styling

---

## Limitations and Future Work

Current or potential limitations:

- Performance may degrade:
  - in noisy environments
  - with very fast or heavily accented speech not seen in training
- Dataset size may be smaller than large commercial datasets.

Planned or possible future work:

- Increase **dataset size** and diversity through more Swecha AP collection drives.
- Support **code-mixed** Telugu–English speech.
- Improve **real-time performance** and streaming recognition.
- Package the system for **deployment** in schools, community centers, and other public spaces.

---

## Contributing

Contributions from **Swecha AP members**, other Swecha chapters, and the wider free software community are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/my-improvement
   ```

3. Commit your changes:

   ```bash
   git commit -am "Improve Telugu ASR pipeline"
   ```

4. Push the branch:

   ```bash
   git push origin feature/my-improvement
   ```

5. Open a Pull Request.

Ways to help:

- Improve the code (frontend/backend).
- Enhance documentation and examples.
- Contribute Telugu test cases and evaluation data.
- Work on training scripts or model optimization.

---

## License

Specify how the **code**, **model**, and **data** are licensed.

Example:

```text
This project is licensed under the MIT License - see the LICENSE file for details.
```

If the collected voice data has different conditions (e.g., only for research / non-commercial use), document that explicitly.

---

## Acknowledgements

- **Swecha AP (Swecha Andhra Pradesh)** community for initiating and driving this project.
- All **volunteers and contributors** who donated their Telugu voice samples and time.
- The broader **Swecha** movement for promoting free software, free culture, and local language technology.
- Developers and maintainers of **Whisper**, PyTorch, and other open-source tools that made this possible.

---
