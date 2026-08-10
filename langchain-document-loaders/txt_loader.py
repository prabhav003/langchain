from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a summary for the following problem \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

# print(docs)

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser 

result = chain.invoke({'poem':docs[0].page_content})

print(result)

'''
Here is a summary of the problem:

The poem "The Spirit of Cricket" is a celebration of the game of cricket, highlighting the excitement and passion of the sport. Itdescribes the players in action, the thrill of a well-played shot, and the joy of the game being shared with the crowd. The poem also emphasizes the importance of sportsmanship and the spirit of competition, suggesting that the game is about giving one's best effort and respecting one's opponents, regardless of the outcome.
'''


# python txt_loader.py