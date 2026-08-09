# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate

# llm = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     temperature=0.7
# )

# prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Suggest a catchy blog title about {topic}"
# )

# topic = input("Enter a topic: ")

# formatted_prompt = prompt.format(topic=topic)

# response = llm.invoke(formatted_prompt)

# print("Generated blog title:", response.content)