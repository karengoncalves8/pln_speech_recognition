import speech_recognition as sr

def transcribe_from_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("working microphones", source.list_working_microphones())
        if not source.list_working_microphones():
            print("No working microphones found.")
            return None, None
        print("Listening from microphone...", source.device_index)
        audio = recognizer.listen(source)
        return recognizer, audio

def transcribe_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Reading audio file...")
        audio = recognizer.record(source)
        return recognizer, audio