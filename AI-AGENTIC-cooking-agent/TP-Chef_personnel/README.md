# TP : Agent Chef Cuisinier Personnel

**Master BDCC — SMA et IAD | Prof. RETAL SARA**

## Objectif

Concevoir un agent intelligent jouant le rôle d'un chef cuisinier personnel, capable de :
- Recevoir la liste des ingrédients disponibles
- Mémoriser les préférences et restrictions alimentaires de l'utilisateur
- Utiliser une base de recettes locale (RAG) pour proposer des plats adaptés
- Compléter ses connaissances via une recherche web (Tavily, optionnel)

---

## Structure du projet

```
TP-Chef_personnel/
├── chef_agent.py    # Agent principal avec tous les outils
├── recipes.txt      # Base de recettes locale (15 recettes)
├── pyproject.toml
├── .env.example
└── .gitignore
```

---

## Prérequis

- Python >= 3.10 · [uv](https://docs.astral.sh/uv/) · [Ollama](https://ollama.com/) avec `llama3.2:3b`
- (Optionnel) Clé API Tavily pour la recherche web

```bash
uv sync
cp .env.example .env   # Renseigner TAVILY_API_KEY si disponible
```

---

## Architecture

```
Utilisateur
    |
    v
chef_agent (llama3.2:3b)
    |         |          |            |
    v         v          v            v
search_     search_   remember_   get_
recipes_    web()     preference  preferences
rag()       (Tavily)  (Command)   (ToolRuntime)
    |                     |            |
    v                     v            v
InMemory              ChefState     ChefState
VectorStore           .preferences  .preferences
(recipes.txt)         (update)      (read)
    |
    v
HuggingFace
Embeddings
(all-MiniLM-L6-v2)
```

---

## Composants

### RAG — Base de recettes

`recipes.txt` contient 15 recettes détaillées (couscous, tajine, harira, bricks au thon, baghrir...) découpées en chunks et indexées avec des embeddings sémantiques :

```python
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings)
```

### Mémoire — État persisté

Les préférences utilisateur sont stockées dans un `ChefState` personnalisé, persisté via `InMemorySaver` :

```python
class ChefState(AgentState):
    preferences: list[str]
```

Le tool `remember_preference` met à jour l'état via `Command` :

```python
@tool
def remember_preference(preference: str, runtime: ToolRuntime) -> Command:
    """Store a user preference in long-term memory."""
    current = runtime.state.get("preferences", [])
    return Command(update={
        "preferences": current + [preference],
        "messages": [ToolMessage("Preference saved...", tool_call_id=runtime.tool_call_id)]
    })
```

### Outils disponibles

| Outil | Rôle |
|---|---|
| `search_recipes_rag` | Recherche sémantique dans la base de recettes locale |
| `search_web` | Recherche web via Tavily (nécessite `TAVILY_API_KEY`) |
| `remember_preference` | Sauvegarde une préférence/allergie dans l'état |
| `get_preferences` | Récupère toutes les préférences mémorisées |

---

## Exécution

```bash
uv run --active python chef_agent.py
```

---

## Résultats obtenus

```
User  : J'aime la cuisine marocaine traditionnelle et les plats faits maison.
Chef  : Parfait ! Voici trois recettes qui pourraient vous plaire :
        1. Couscous aux légumes — semoule, carottes, navets, pois chiches
        2. Tajine de kefta — viande hachée, tomates, oeufs
        3. Poulet au citron — citron confit, olives, épices

User  : Je préfère des plats rapides sans viande.
Chef  : Très bien ! Voici des options adaptées :
        1. Salade marocaine — tomates, concombre, citron, huile d'olive
        2. Baghrir — crêpes légères à base de semoule
        3. Gratin de pommes de terre — rapide et simple

User  : J'ai des tomates, de l'huile d'olive, de l'ail et des épices.
Chef  : Vous pouvez préparer :
        - Sauce marocaine simple : faire revenir ail et tomates avec épices
        - Plat rapide : ajouter légumes ou oeufs pour un repas complet

User  : Et si j'ajoute du poulet ?
Chef  : Avec le poulet vous pouvez faire :
        - Tajine de poulet : cuire avec tomates, ail et épices
        - Poulet sauté : cuisson rapide avec huile d'olive et épices

---

## Système Prompt

```python
SYSTEM_PROMPT = """You are a personal chef assistant. Your role is to help users discover
delicious dishes they can prepare with their available ingredients.

You have access to:
- search_recipes_rag: search your local recipe knowledge base
- search_web: search the internet for additional recipes and techniques
- remember_preference: store user preferences, allergies, and dietary restrictions
- get_preferences: retrieve the user's stored preferences

When a user tells you their available ingredients:
1. First check their preferences with get_preferences
2. Search the recipe knowledge base with search_recipes_rag
3. Suggest 2-3 concrete dishes adapted to ingredients and preferences
4. Always respect dietary restrictions and allergies"""
```
