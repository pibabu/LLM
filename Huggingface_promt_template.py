import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'HF_API_KEY'

from langchain import HuggingFaceHub, LLMChain

# initialize Hub LLM
hub_llm = HuggingFaceHub(
        repo_id='google/flan-t5-xl',
    model_kwargs={'temperature':1e-10}
)

# create prompt template > LLM chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)
question = "    "

print(llm_chain.run(question))