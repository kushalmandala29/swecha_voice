from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torchaudio
import torch


class Model:
    def __init__(self,):
        self.processor = AutoProcessor.from_pretrained("swechatelangana/whisper-small-te-146h")
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained("swechatelangana/whisper-small-te-146h")
    def translate(self,speech_array,sampling_rate):
        # Resample the audio to 16kHz if needed
        if sampling_rate != 16000:
            resampler = torchaudio.transforms.Resample(sampling_rate, 16000)
            speech_array = resampler(speech_array)
        
        input_features = self.processor(speech_array.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_features
# Generate the transcription
        with torch.no_grad():
            predicted_ids = self.model.generate(input_features)
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

        return transcription