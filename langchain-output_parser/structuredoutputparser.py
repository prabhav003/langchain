from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'blackhole'})

# result = model.invoke(prompt)

# result = parser.parse(result.content)

# print(result)

chain = template | model | parser 

result = chain.invoke({'topic':'blackhole'})

print(result)





# python structuredoutputparser.py