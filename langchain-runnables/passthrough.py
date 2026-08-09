from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke \n {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'exlaination': RunnableSequence(prompt2, model, parser)
    }
) 

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'cricket'})

print(result)



'''
{
'joke': 'Why did the cricket go to the doctor?\n\nBecause it had a ball to deal with.',

'exlaination': 'A clever play on words!\n\nThe joke is a pun, which is a form of wordplay that exploits multiple meanings of a word or phrase. In this case, the punchline "it had a ball to deal with" has a double meaning:\n\n1. "A ball" can refer to a physical object, like a sphere or a cricket ball (atype of ball used in the sport of cricket).\n2. "A ball to deal with" is also a common idiomatic expression that means "a problem to handle" or "a difficult situation to manage".\n\nThe joke is funny because it takes the expected meaning of the phrase "a ball to deal with" (a problem to handle) and gives it a clever twist by referencing the cricket ball, which is a play on the fact that the cricket (the insect) is the subject of the joke. It\'s a clever and silly pun that creates the humor!'
}
'''