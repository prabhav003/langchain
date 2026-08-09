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




# Prompt class
class NakliPromptTemplate(Runnable):
    def __init__(self,template, input_variables):
        self.template = template
        self.input_variables = input_variables 

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    



# stroutput
class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']


# runnableconnector 
class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data    


template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Write a explaination about joke \n {response}',
    input_variables=['response']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

result = final_chain.invoke({'topic':'cricket'})

print(result)








# python multichain.py
