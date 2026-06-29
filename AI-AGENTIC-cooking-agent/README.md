# AI Agentic — Master BDCC

Depot unique regroupant tous les Labs et TPs du module **SMA et IAD — Master BDCC | Prof. RETAL SARA**.

## Structure

| Dossier | Sujet |
|---|---|
| [Lab1-prompt-engineering](./Lab1-prompt-engineering) | Ingenierie des prompts (tokenisation, Ollama, Groq, OpenAI, JSON, images) |
| [Lab2-langchain-agents](./Lab2-langchain-agents) | Agents avec LangChain (agent chef personnel, memoire, web search) |
| [Lab3-RAG](./Lab3-RAG) | RAG sur PDF (HuggingFace embeddings) + agent SQL (Chinook DB) |
| [Lab4-MCP](./Lab4-MCP) | Model Context Protocol : stdio, serveur de temps, HTTP streaming |
| [Lab5-LangGraph_Studio](./Lab5-LangGraph_Studio) | LangGraph Studio (visualisation/debug d'agents) + systeme Multi-Agents hierarchique |
| [Lab6-Contexte_et_Etat](./Lab6-Contexte_et_Etat) | Contexte par invocation (`ReaderProfile`) et etat persiste (`LibraryState`) |
| [Lab7-Human_In_The_Loop](./Lab7-Human_In_The_Loop) | Agent HITL : interrupt(), approve / reject / edit |
| [Lab8-Workflow_avec_LangGraph](./Lab8-Workflow_avec_LangGraph) | Workflows LangGraph : graphe simple, reducers, etat message, branchements conditionnels, boucles |
| [Lab9-Agent_avec_LangGraph](./Lab9-Agent_avec_LangGraph) | Agent LangGraph : tools, agent comme noeud, HITL fonctionnel (`@entrypoint`/`@task`), historique et fork |
| [TP-Chef_personnel](./TP-Chef_personnel) | Agent chef cuisinier : RAG + memoire + recherche web + system prompt |

## Prerequis communs

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/) — gestionnaire de paquets
- [Ollama](https://ollama.com/) avec le modele `llama3.2:3b`

```bash
ollama pull llama3.2:3b
```

## Execution

Chaque lab est autonome avec son propre environnement virtuel :

```bash
cd Lab6-Contexte_et_Etat
uv sync
uv run --active python agent_context.py
uv run --active python agent_state.py
```

## Remarques

- Les fichiers `.env` ne doivent pas etre pushes sur GitHub (voir `.env.example` dans chaque lab).
- Certains labs demandent des cles API optionnelles (`TAVILY_API_KEY`, `LANGSMITH_API_KEY`).
