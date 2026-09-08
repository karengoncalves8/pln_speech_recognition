from services import _recognize_audio, transcribe_from_microphone, transcribe_from_file


def main():
    print("==== Transcrição de Áudio ====")

    choice = input("Escolha a fonte de áudio (1: Microfone, 2: Arquivo): ")
    if choice == "1":
        recognizer, audio = transcribe_from_microphone()
        _recognize_audio(recognizer, audio)
    elif choice == "2":
        file_path = input("Digite o caminho do arquivo de áudio: ")
        recognizer, audio = transcribe_from_file(file_path)
        _recognize_audio(recognizer, audio)
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


if __name__ == "__main__":
    main()
