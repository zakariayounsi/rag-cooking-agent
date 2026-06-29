# TP Ingenierie des Prompts

Projet structure a partir du document `1 TP Ingenierie des prompts.docx`.

## Contenu

- `01_tokenisation.py` : tokenisation avec `tiktoken`
- `02_ollama_prompt.py` : prompt simple avec Ollama
- `03_groq_prompt.py` : prompt simple avec Groq
- `04_openai_prompt.py` : prompt simple avec OpenAI
- `05_aspect_sentiment_json.py` : analyse de sentiment avec sortie JSON
- `06_image_generation.py` : generation d'image
- `07_image_description.py` : description de `rag.png`

## Installation avec uv

```bash
uv venv
uv sync
```

Activation de l'environnement :

Sous Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Sous bash :

```bash
source .venv/bin/activate
```

## Configuration

Copier `.env.example` vers `.env`, puis renseigner :

```env
OPENAI_API_KEY=...
GROQ_API_KEY=...
OLLAMA_MODEL=llama3.2:3b
```

## Execution

Chaque script se lance separement :

```bash
python 01_tokenisation.py
python 02_ollama_prompt.py
python 03_groq_prompt.py
python 04_openai_prompt.py
python 05_aspect_sentiment_json.py
python 06_image_generation.py
python 07_image_description.py
```

## Notes

- `01_tokenisation.py` ne demande aucune cle API.
- `02_ollama_prompt.py` demande un serveur Ollama actif et un modele local installe.
- `03` a `07` demandent des cles API valides.
