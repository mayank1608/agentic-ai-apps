from ollama import chat

print(f"Ollama test running");
response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Who has the highest salary?'
        }
    ]
)

print(response['message']['content'])