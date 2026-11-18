import whisper

print("Loading model...")

model = whisper.load_model("small")

print("Transcribing...")

result = model.transcribe(
    "voice.mp3",
    language="en"
)

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Done! Saved to transcription.txt")
#test
