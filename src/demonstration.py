import spacy

from services.recognize import _recognize_audio
from services.transcribe import transcribe_from_file

# Carrega o modelo de Processamento de Linguagem Natural para o português
nlp = spacy.load("pt_core_news_sm")

# file_path = "C:\\Users\\Karen-Autaza\\Documents\\Personal\\pln\\pt_speech_recognition\\src\\assets\\demonstracao.wav"
# recognizer, audio = transcribe_from_file(file_path)
# texto_reconhecido = _recognize_audio(recognizer, audio)

# 1. Entrada ideal (Simulando um texto humano bem formatado ou corrigido)
texto_ideal = "A Rosa foi morar em Curitiba. Você a conhece?"

# 2. Saída bruta do STT (Sem maiúsculas e sem pontuação)
texto_reconhecido = "a rosa foi morar em curitiba você a conhece"

def analisar_texto(rotulo, texto):
    print(f"\n--- {rotulo} ---")
    print(f"Texto bruto: \"{texto}\"\n")
    
    doc = nlp(texto)
    
    # Demonstração 1: Tokenização de Sentenças
    print("1. Sentenças detectadas:")
    sentencas = list(doc.sents)
    for i, sent in enumerate(sentencas, 1):
        print(f"   Sentença {i}: [{sent.text}]")
    if len(sentencas) <= 1:
        print("   -> ALERTA: O tokenizador falhou em separar as frases!")

    # Demonstração 2: Reconhecimento de Entidades Nomeadas (NER)
    print("\n2. Entidades Nomeadas (NER) encontradas:")
    if doc.ents:
        for ent in doc.ents:
            print(f"   - Entidade: '{ent.text}' | Tipo: {ent.label_}")
    else:
        print("   -> ALERTA: Nenhuma entidade nomeada foi encontrada!")

# Executa a análise para ambos os casos
analisar_texto("CASO A: Texto Ideal (Com Casing e Pontuação)", texto_ideal)
analisar_texto("CASO B: Saída do STT (Sem Casing e Pontuação)", texto_reconhecido)

# O problema: A palavra "rosa" em minúsculas deixa de ser tratada como o nome próprio de uma pessoa e passa a ser interpretada pelo modelo como o substantivo comum "rosa" (a flor).
# Como consequência, o modelo perde a entidade PER completamente!