from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template =  PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# result = parser.parse(result.content)

# print(result)

# print(type(result))


chain = template | model | parser

result = chain.invoke({'topic':'blackhole'})

print(result)





'''
{'fact1': {'description': 'Black holes are regions in space where the gravitational pull is so strong that nothing, not even light, can escape.', 'additional_info': 'They are formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime.'}, 

 'fact2': {'description': "The point of no return around a black hole is called the event horizon. Once you cross the event horizon, you are trapped by theblack hole's gravity and cannot escape.", 'additional_info': 'The event horizon is not a physical boundary, but rather a mathematical concept that marks the point at which the gravitational pull becomes so strong that escape isimpossible.'}, 

 'fact3': {'description': 'Black holes come in different sizes, ranging from small, stellar-mass black holes formed from the collapse of individual stars, to supermassive black holes found at the centers of galaxies, with masses millions or even billions of times that of the Sun.', 'additional_info': 'The largest known black hole has a mass of approximately 40 billion solar masses.'}, 

 'fact4': {'description': 'The singularities at the center of black holes are points of infinite density and zero volume, where the laws of physics as we know them break down.', 'additional_info': 'The curvature of spacetime around a black hole is so extreme that not even the laws of quantum mechanics can describe what happens at the singularity.'}, 

 'fact5': {'description': "Despite their reputation as cosmic monsters, black holes are actually very useful for astronomers. By observing the motion of stars and gas around a black hole, scientists can learn about the black hole's mass and spin.", 'additional_info': 'Black holes are also thought to be responsible for the most powerful cosmic events, such as gamma-ray bursts and active galactic nuclei.'}}

 '''