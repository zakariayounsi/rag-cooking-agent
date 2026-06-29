"""Genere une visualisation du graphe LangGraph (graph.mmd et graph.png).

Lancer avec : uv run python generate_graph.py
"""
from pathlib import Path

from src.graph import graph

BASE_DIR = Path(__file__).resolve().parent
MERMAID_PATH = BASE_DIR / "graph.mmd"
PNG_PATH = BASE_DIR / "graph.png"


def main() -> None:
    mermaid_source = graph.get_graph().draw_mermaid()
    MERMAID_PATH.write_text(mermaid_source, encoding="utf-8")
    print(f"Source Mermaid ecrite dans {MERMAID_PATH}")

    try:
        png_bytes = graph.get_graph().draw_mermaid_png()
        PNG_PATH.write_bytes(png_bytes)
        print(f"Image du graphe ecrite dans {PNG_PATH}")
    except Exception as exc:
        print(f"Impossible de generer le PNG ({exc}). Utilisez {MERMAID_PATH} sur https://mermaid.live")


if __name__ == "__main__":
    main()
