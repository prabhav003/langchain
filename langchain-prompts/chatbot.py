from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant.')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)

print(chat_history)    


# '''
# [SystemMessage(content='You are a helpful AI assistant.', additional_kwargs={}, response_metadata={}),

#  HumanMessage(content='Hi', additional_kwargs={}, response_metadata={}), 
 
#  AIMessage(content="It's nice to meet you. Is there something I can help you with or would you like to chat?", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), 
 
#  HumanMessage(content='What is the color of grass', additional_kwargs={}, response_metadata={}), 
 
#  AIMessage(content="The color of grass can vary depending on the type of grass and the environment it's in. However, in general, most types of grass are green.\n\nIn particular, the color of grass is often described as:\n\n* A medium to dark green (e.g., lawn grass, like Kentucky bluegrass or perennial ryegrass)\n* A lighter green (e.g., wheat grass or some types of wild grasses)\n* A bluish-green (e.g., some types of tropical grasses or certain varieties of ornamental grasses)\n\nKeep in mind that the color of grass can also be affected by factors like soil quality, sunlight, water, and fertilization. But overall, green is the dominant color associated with grass!", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), 
 
#  HumanMessage(content='is it venemous', additional_kwargs={}, response_metadata={}), 
 
#  AIMessage(content="No, grass is not venomous. In fact, grass is a type of plant that is generally safe to touch, walk on, or even eat (although it's not recommended to eat large quantities of grass, as it can cause stomach upset).\n\nWhile some grasses may have sharp edges or points, and a few species may have irritating or allergenic properties, most grasses are harmless to humans.\n\nIt's worth noting that some plants in the grass family (Poaceae) can be toxic or cause allergic reactions in some people, but this is not due to the grass being venomous. For example, some types of grass may contain high levels of oxalates, which can be toxic in large quantities.\n\nSo, rest assured, grass is not venomous, and it's generally a safe and pleasant part of our environment!", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]

# '''