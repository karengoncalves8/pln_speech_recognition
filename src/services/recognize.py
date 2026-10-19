import speech_recognition as sr

def _recognize_audio(recognizer, audio, language="pt-BR"):
    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")