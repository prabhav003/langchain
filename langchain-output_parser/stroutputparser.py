from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# 1st prompt

template1 =  PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt

template2 =  PromptTemplate(
    template='Write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic':'blackhole'})

print(result)


# Here is a 5-line summary of the text:

# Black holes are regions of spacetime with such strong gravitational pull that not even light can escape. They are formed when a massive star collapses in on itself, creating an intense gravitational field. There are four types of black holes, classified by their mass and the nature of the matter that forms them. Black holes have unique properties, including an event horizon, singularity, ergosphere, and Hawking radiation. Understanding black holes has captivated scientists and the public alike, and continues to be a topic of ongoing research and exploration.
