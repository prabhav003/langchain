from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Generate 5 facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({'topic':'Anime'})

print(result)

chain.get_graph().print_ascii()



# =======================
#         output
# =======================

'''
Here are five interesting facts about anime:

1. **The word "anime" was coined in the West**: While anime has been a part of Japanese culture for over a century, the term "anime" itself was first used in the West to describe Japanese animation. The word "anime" comes from the French word "animé," which was used to describe animated films. However, in Japan, the term "anime" is not commonly used, and instead, the term "manga" (for comics) and "anime" (for animation) are used to describe the medium.

2. **Anime has a global following**: Despite being a product of Japanese culture, anime has gained a massive following worldwide, with fans from diverse backgrounds and cultures. In fact, anime has become a significant export for Japan, with many anime series and films being dubbed or subtitled in multiple languages and distributed globally.

3. **The first anime film was made in 1917**: The first anime film, "Katsudō Shashin" (or "Humorous Phases of Funny Faces"), was created in 1917 by Japanese filmmaker Ōten Shimokawa. This early anime film was a short, humorous animation that featured a character with a distorted face. While it may seem simple by today's standards, this early experiment marked the beginning of a long and rich history of anime production.

4. **Anime is not just for kids**: While many people associate anime with children's shows, the reality is that anime has a wide range of themes, genres, and audiences. From action-packed mecha series like "Neon Genesis Evangelion" to thought-provoking psychological thrillers like "Death Note," anime covers a broad spectrum of genres and appeals to a diverse range of audiences.

5. **Anime has a significant economic impact**: The anime industry is a significant contributor to Japan's economy, with the country's anime and manga industry generating over $20 billion in revenue each year. This revenue comes not just from the sale of anime series and films, but also from the merchandising of anime characters, games, and other related products.
'''


# python simple_chain.py