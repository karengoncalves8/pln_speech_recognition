# PT Speech Recognition

Projeto acadêmico (FATEC, disciplina de Processamento de Linguagem Natural) que transcreve áudio em português para texto e mostra como a qualidade dessa transcrição afeta tarefas de PLN.

## O que a aplicação faz

O projeto tem duas partes:

1. **Transcrição de áudio** ([src/main.py](src/main.py)): captura áudio do microfone ou lê um arquivo `.wav` e o converte em texto em português (`pt-BR`) com a biblioteca [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), que usa a API de reconhecimento de fala do Google.

2. **Demonstração de PLN** ([src/demonstration.py](src/demonstration.py)): compara a análise do [spaCy](https://spacy.io/) sobre dois textos com o mesmo conteúdo:
   - **Caso A**, texto ideal, com letras maiúsculas e pontuação: `"A Rosa foi morar em Curitiba. Você a conhece?"`
   - **Caso B**, texto como sai de um sistema de reconhecimento de fala (STT), sem maiúsculas e sem pontuação: `"a rosa foi morar em curitiba você a conhece"`

   Para cada caso, o script mostra:
   - **Segmentação de sentenças**: sem pontuação, o modelo não consegue separar as frases.
   - **Reconhecimento de Entidades Nomeadas (NER)**: com "rosa" em minúsculas, o modelo passa a tratá-la como o substantivo comum (a flor) e deixa de reconhecer a pessoa (`PER`).

   A conclusão é que a saída bruta de um STT prejudica etapas seguintes do PLN, e que restaurar maiúsculas e pontuação é um pré-processamento importante.

### Estrutura

```
src/
├── main.py                 # Programa interativo de transcrição (microfone ou arquivo)
├── demonstration.py        # Demonstração do impacto do STT no spaCy
├── services/
│   ├── transcribe.py       # Captura de áudio (microfone / arquivo)
│   └── recognize.py        # Envio do áudio à API do Google e retorno do texto
└── assets/                 # Áudios .wav de exemplo
    ├── amguidade.wav
    ├── demonstracao.wav
    └── pontuacao.wav
```

## Pré-requisitos

- **Python 3.12** ou superior
- **[uv](https://docs.astral.sh/uv/)** para gerenciar o ambiente e as dependências (recomendado)
- **Conexão com a internet**: a transcrição usa a API do Google
- **Microfone**, apenas se for transcrever pela opção de microfone

Para instalar o `uv`:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Instalação

1. Clone o repositório e entre na pasta:

   ```bash
   git clone <url-do-repositorio>
   cd pln_speech_recognition
   ```

2. Instale as dependências (`speechrecognition`, `pyaudio` e `spacy`). O `uv` cria o ambiente virtual `.venv` automaticamente:

   ```bash
   uv sync
   ```

3. Baixe o modelo de português do spaCy, usado pela demonstração:

   ```bash
   uv run spacy download pt_core_news_sm
   ```


### Sem o uv

Se preferir usar `pip`:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install speechrecognition pyaudio spacy
python -m spacy download pt_core_news_sm
```

### Problemas com o PyAudio

O `pyaudio` só é necessário para a captura pelo microfone. Se a instalação falhar:

- **Windows**: em geral, o `pip`/`uv` baixa um pacote pronto. Se não baixar, atualize o Python para uma versão com suporte.
- **Linux (Debian/Ubuntu)**: `sudo apt install portaudio19-dev python3-dev` e instale de novo.
- **macOS**: `brew install portaudio` e instale de novo.

## Como rodar

Os scripts importam o pacote `services` de forma relativa à pasta `src`, então **execute-os de dentro de `src/`**:

```bash
cd src
```

### Transcrição de áudio

```bash
uv run main.py
```

O programa pergunta qual fonte usar:

- **`1` (Microfone)**: ajusta o ruído ambiente por 1 segundo, escuta até você parar de falar e mostra o texto transcrito.
- **`2` (Arquivo)**: pede o caminho de um arquivo de áudio (`.wav`, `.aiff` ou `.flac`). Para testar, use um dos exemplos:

  ```
  Digite o caminho do arquivo de áudio: assets/pontuacao.wav
  ```

Exemplo de saída:

```
==== Transcrição de Áudio ====
Escolha a fonte de áudio (1: Microfone, 2: Arquivo): 2
Digite o caminho do arquivo de áudio: assets/demonstracao.wav
Reading audio file...
Transcription: ...
```

### Demonstração de PLN

```bash
uv run python demonstration.py
```

O script analisa os casos A e B e mostra as sentenças e as entidades encontradas em cada um. No caso B aparecem alertas de que o tokenizador não separou as frases e de que nenhuma entidade foi encontrada.

Para analisar a transcrição real de um áudio em vez do texto fixo, descomente estas linhas em [src/demonstration.py](src/demonstration.py) e ajuste o caminho:

```python
file_path = "assets/demonstracao.wav"
recognizer, audio = transcribe_from_file(file_path)
texto_reconhecido = _recognize_audio(recognizer, audio)
```

## Tecnologias

| Biblioteca | Uso |
|---|---|
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Captura e transcrição de áudio (Google Web Speech API) |
| [PyAudio](https://pypi.org/project/PyAudio/) | Acesso ao microfone |
| [spaCy](https://spacy.io/) + `pt_core_news_sm` | Segmentação de sentenças e NER em português |
