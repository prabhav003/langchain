# model downloads locally 
# need good local machine config


from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-0.6B",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke('What is the capital of India?')

print(result.content)