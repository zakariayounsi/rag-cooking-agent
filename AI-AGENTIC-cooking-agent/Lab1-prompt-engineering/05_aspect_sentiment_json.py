import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(override=True)

system_message = """
Effectuez une analyse de sentiments basee sur les aspects des avis concernant
les ordinateurs portables presentes en entree.

Chaque avis peut comporter un ou plusieurs des aspects suivants : screen,
keyboard et pad.

Pour chaque avis presente en entree :
- Identifiez la presence d'au moins un des trois aspects.
- Attribuez une polarite de sentiment (positive, negative ou neutral)
  a chaque aspect.
- Organisez votre reponse dans un objet JSON avec les cles suivantes :
  - category : liste des aspects
  - polarity : liste des polarites correspondantes
- Si l'un des aspects n'est pas present dans l'avis, supposez que sa
  polarite est neutral.
"""

llm = ChatOpenAI(
    model="gpt-5.2",
    temperature=0,
    model_kwargs={"response_format": {"type": "json_object"}},
)

resp = llm.invoke(
    [
        {"role": "system", "content": system_message},
        {
            "role": "user",
            "content": "L'ecran est tres bon, mais je n'ai pas aime le pad. Le clavier est acceptable.",
        },
    ]
)

print(resp.content)

result = json.loads(resp.content)
print("\nJSON parse:", result)
print("Premiere polarite:", result["polarity"][0])
