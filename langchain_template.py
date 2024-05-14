from langchain_community.llms import GPT4All
from langchain_community.llms import PromptTemplate, LLMChain

# create a prompt template where it contains some initial instructions
# here we say our LLM to think step by step and give the answer

template = """
Let's think step by step of the question: {question}
Based on all the thought the final answer becomes:
"""
prompt = PromptTemplate(template=template, input_variables=["question"])


local_path = ("./models/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin")


llm = GPT4All(
    model=local_path, 
    backend="llama", 
)

llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)


llm_chain('Jesus last day, told by terry pratchett')