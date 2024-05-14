#Run LLM locally with ChatGPT via OpenAPI 

#### !  run with openai==0.28    -  openai.completion....() nicht höher supported !

import openai

openai.api_base = "http://localhost:4891/v1"
#openai.api_base = "https://api.openai.com/v1"

openai.api_key = "egal"
 
prompt = "jesus last day, told by tarantino - tell only the story"

# model = "gpt-3.5-turbo"
#model = "mpt-7b-chat"
model = ""    # nimmt laufendes model in gpt4all

# make API request
response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=70, ## ok
    temperature=0.28,  ## the lower the temperature, the more deterministic
    n=1,
    echo=True,
    stream=False
)


print(response)