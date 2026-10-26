import speech_recognition as sr

# Utiliza como arquitetura as Redes Neurais Recorrentes, as quais possuem "memória" e analisam o áudio de forma sequencial e contínua, 
# permitindo entender o som com base no que veio imediatamente antes e depois.

def _recognize_audio(recognizer, audio, language="pt-BR"):
    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")