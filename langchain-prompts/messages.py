from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessage(content='Tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)


'''
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}), 

HumanMessage(content='Tell me about langchain', additional_kwargs={}, response_metadata={}), 

AIMessage(content='LangChain is a new language model architecture developed by Meta AI, which is designed to enable more efficient and effective knowledge acquisition and reasoning processes. Here\'s a high-level overview of LangChain:\n\n**Key Features:**\n\n1.**Modular Architecture**: LangChain is composed of multiple modules, each responsible for a specific task, such as knowledge acquisition, reasoning, and text generation. This modularity allows for more efficient processing and easier tuning of individual components.\n2. **Efficient Knowledge Acquisition**: LangChain\'s knowledge acquisition module uses a novel approach called "query-conditioned learning" to efficiently acquire knowledge from large datasets. This method enables the model to focus on relevant information and adapt to new data more quickly.\n3. **Improved Reasoning Capabilities**: LangChain\'s reasoning module uses a combination of symbolic and neural-based reasoning methods to improve the model\'s ability to reason about complex topics and generate accurate responses.\n4.**Enhanced Text Generation**: LangChain\'s text generation module is designed to produce more coherent, informative, and engaging responses, leveraging the knowledge acquired through the model\'s reasoning capabilities.\n\n**Advantages:**\n\n1. **Improved Efficiency**: LangChain\'s modular architecture and efficient knowledge acquisition methods enable the model to process and respond to queries more quickly, making it suitable for real-time applications.\n2. **Enhanced Reasoning**: The model\'s improved reasoning capabilities enable it to generate more accurate and informative responses, even when faced with complex or ambiguous queries.\n3. **Flexibility**: LangChain\'s modular design allows for easy integration with various datasets, tasks, and applications, making it a versatile andadaptable model.\n\n**Applications:**\n\n1. **Virtual Assistants**: LangChain\'s advanced knowledge acquisition and reasoning capabilities make it an excellent candidate for virtual assistants, enabling them to provide more accurate and informative responses to user queries.\n2. **Knowledge Graphs**: The model\'s ability to efficiently acquire and reason about complex knowledge makes it suitable for building and maintaining large knowledge graphs.\n3.**Chatbots and Conversational AI**: LangChain\'s improved text generation capabilities and reasoning abilities enable it to engage in more natural and informative conversations with users.\n\nOverall, LangChain is a promising language model architecture that has the potential to improve the efficiency and effectiveness of various AI applications, including virtual assistants, knowledge graphs, and chatbots.', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]
'''