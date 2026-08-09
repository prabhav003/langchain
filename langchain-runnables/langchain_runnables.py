import random
from abc import ABC, abstractmethod



# runnable
class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass




# LLM class
class NakliLLM(Runnable):
    def __init__(self):
        print('LLM Created')

    def invoke(self, prompt):
        response_list=[
            'Delhi is the capital of India.',
            'IPL is a cricket legue',
            'AI stands for artificial intelligence'
        ]    
    
        return {'response': random.choice(response_list)}

    def predict(self, prompt):
        response_list=[
            'Delhi is the capital of India.',
            'IPL is a cricket legue',
            'AI stands for artificial intelligence'
        ]    

        return {'response': random.choic(response_list)}  




# print(llm.predict('What is the capital of India.'))

# Prompt class
class NakliPromptTemplate(Runnable):
    def __init__(self,template, input_variables):
        self.template = template
        self.input_variables = input_variables 

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    


# prompt = template.format({'topic':'india', 'length':'short'})

# print('prompt: ',prompt)

# print(llm.predict(prompt))


# # chain class
# class NakliLLMChain:
#     def __init__(self, llm, prompt):
#         self.llm = llm
#         self.prompt = prompt

#     def run(self, input_dict):
#         final_prompt = self.prompt.format(input_dict)
#         result = self.llm.predict(final_prompt)

#         return result['response']

# chain = NakliLLMChain(llm, template)

# print(template.format({'topic':'india', 'length':'short'}))
# print(chain.run({'topic':'india', 'length':'short'}))


class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']


class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data    

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['topic','length']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain = RunnableConnector([template, llm, parser])

result = chain.invoke({'topic':'india', 'length':'short'})
print(result)






# python langchain_runnables.py