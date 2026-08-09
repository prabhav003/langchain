from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkedin': RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])




'''
{
 'tweet': 'Here\'s a tweet about AI:\n\n"Artificial Intelligence is no longer the stuff of sci-fi! From virtual assistants to self-driving cars, AI is transforming our world. What\'s the most exciting AI innovation you\'ve seen recently? #AI #Tech #Innovation"',

 'linkedin': 'Here\'s a potential LinkedIn post about AI:\n\n**Headline:** "The Future of Work: How AI is Revolutionizing Industries and Transforming Careers"\n\n**Post:**\n\nAs AI continues to shape the world around us, it\'s essential to stay ahead of the curve. From transforming industries to revolutionizing the way we work, AI is no longer just a buzzword - it\'s a reality that\'s changing the game.\n\n**Did you know:**\n\n* By 2025, AI will create 58% more jobs than it displaces, according to a report by Gartner\n* AI is expected to add $2.3 trillion to the global economy by 2025, according to a report by PwC\n* 70% of organizations say AI will significantly impact their business, according to a report by Accenture\n\n**But what does this mean for you?**\n\nAs AI continues to advance, it\'s essential to develop skills that complement its capabilities. From data science to machine learning, and fromprogramming to UX design, the demand for professionals with AI expertise is on the rise.\n\n**What can you do to stay ahead?**\n\n* Invest in AI-related training and education\n* Network with professionals in the AI space\n* Stay up-to-date on the latest AI trends and breakthroughs\n\n**Let\'s continue the conversation:**\n\nWhat are your thoughts on the impact of AI on the future of work?How are you preparing for the AI revolution? Share your insights and let\'s connect!\n\n**#AI #FutureOfWork #Innovation #CareerDevelopment**\n\nFeel free to modify it to fit your style and tone!'
}'''