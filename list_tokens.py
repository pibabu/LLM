from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
tokens = []
with model.chat_session():
    for token in model.generate("write as richard stark: the last day of jesus", streaming=True):
        tokens.append(token)
print(tokens)