from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following questions \n {question} from the following text \n {text}',
    input_variables=['question','text']
)

url = 'https://www.flipkart.com/apple-macbook-air-m4-24-gb-512-gb-ssd-macos-sequoia-mc7d4hn-a/p/itm2814d44889ee9?pid=COMH9ZWQSAU7H4TG&lid=LSTCOMH9ZWQSAU7H4TGHNJW6M&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=bec6a407-1fe2-4f29-a838-21216af2549b.COMH9ZWQSAU7H4TG.SEARCH&ppt=hp&ppn=homepage&ssid=5aff7d3uu80000001786468200593&qH=864faee128623e2f&ov_redirect=true'

loader = WebBaseLoader(url)

docs = loader.load()

question = 'Tell me the price of the product.'

chain = prompt | model | parser 

result = chain.invoke({'question':question, 'text':docs[0].page_content})

print(result)