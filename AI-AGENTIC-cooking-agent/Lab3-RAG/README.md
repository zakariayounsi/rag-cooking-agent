# LAB 3 : Retrieval-Augmented Generation (RAG)

**Master BDCC — SMA et IAD | Prof. RETAL SARA**

## Objectif

Implémenter le pattern **RAG (Génération Augmentée par Récupération)** avec LangChain pour permettre à un agent LLM de répondre à des questions en se basant sur des sources de données externes : un fichier PDF et une base de données SQL.

---

## Structure du projet

```
Lab3-RAG/
├── part1_rag_pdf.py               # Partie 1 : Agent RAG sur PDF
├── part2_sql_agent.py             # Partie 2 : Agent SQL sur SQLite
├── acmecorp-employee-handbook.pdf # Document source (employee handbook)
└── Chinook.db                     # Base de données SQLite (musique)
```

---

## Prérequis

- Python >= 3.10
- [Ollama](https://ollama.com/) avec `llama3.2:3b` (`ollama pull llama3.2:3b`)
- Dépendances installées :

```bash
pip install langchain langchain-community langchain-ollama langgraph \
            sentence-transformers pypdf sqlalchemy
```

---

## Partie 1 — Agent RAG sur fichier PDF

**Fichier :** `part1_rag_pdf.py`

### Pipeline RAG

```
PDF → Chargement → Segmentation → Embeddings → VectorStore → Recherche sémantique → Agent
```

### Étapes détaillées

| Étape | Outil | Description |
|---|---|---|
| Chargement | `PyPDFLoader` | Extrait le texte page par page |
| Segmentation | `RecursiveCharacterTextSplitter` | Découpe en chunks (1000 chars, overlap 200) |
| Embeddings | `HuggingFaceEmbeddings` (all-MiniLM-L6-v2) | Vectorise chaque chunk |
| Vector Store | `InMemoryVectorStore` | Stocke et indexe les vecteurs en mémoire |
| Recherche | `similarity_search()` | Retrouve les chunks les plus pertinents |
| Agent | `create_react_agent` + `search_handbook` tool | Répond aux questions via RAG |

### Exécution

```bash
python part1_rag_pdf.py
```

### Résultat attendu

```
Pages chargées : N
Nombre de chunks : N
Documents indexés : N

--- Résultat de la recherche sémantique ---
page_content='... vacation policy ...' metadata={'page': X, ...}

--- Réponse de l'Agent RAG ---
Based on the employee handbook, employees in their first year receive X days of vacation...
```

### Architecture de l'agent RAG

```
User question
     │
     ▼
  Agent LLM (llama3.2:3b)
     │
     └── tool: search_handbook(query)
                    │
                    ▼
           InMemoryVectorStore
           similarity_search()
                    │
                    ▼
           chunk le plus proche
           (acmecorp-employee-handbook.pdf)
                    │
                    ▼
           Réponse contextualisée
```

---

## Partie 2 — Agent SQL sur base SQLite

**Fichier :** `part2_sql_agent.py`  
**Base de données :** `Chinook.db` (base musicale — artistes, albums, tracks, etc.)

### Pipeline SQL Agent

```
Question NL → Agent LLM → sql_query tool → SQLite → Résultat → Réponse NL
```

### Exécution

```bash
python part2_sql_agent.py
```

### Résultat attendu

```
--- Test du tool sql_query ---
[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), ...]

--- Réponse de l'Agent SQL ---
Here are the first 5 artists in the database:
1. AC/DC
2. Accept
3. Aerosmith
4. Alanis Morissette
5. Alice In Chains
```

### Schéma de la base Chinook utilisé

```sql
Table Artist:
  - ArtistId  INTEGER (PK)
  - Name      TEXT
```

### System prompt de l'agent SQL

L'agent est configuré avec des règles strictes :
- Utiliser **uniquement** le tool `sql_query`
- Ne pas deviner — si l'information n'existe pas, le dire
- Retourner les résultats en **langage naturel lisible**

---

## Comparaison des deux approches

| | Partie 1 — RAG PDF | Partie 2 — SQL Agent |
|---|---|---|
| **Source** | Fichier PDF | Base SQLite |
| **Indexation** | Embeddings vectoriels | Pas d'indexation |
| **Recherche** | Similarité sémantique | Requêtes SQL exactes |
| **LLM role** | Synthèse du contexte récupéré | Génération de requêtes SQL |
| **Meilleur pour** | Questions ouvertes sur documents | Données structurées précises |

---

## Concept RAG

```
Sans RAG :   Question → LLM (connaissance limitée) → Réponse potentiellement incorrecte

Avec RAG :   Question → Retrieval (documents pertinents)
                              │
                              ▼
                    LLM + Contexte récupéré → Réponse précise et sourcée
```
