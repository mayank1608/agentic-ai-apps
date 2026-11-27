from agents.sql_agent import SQLAgent

agent = SQLAgent()

print("\n========== Gemini SQL Agent ==========")

while True:

    question = input("\nAsk Question or type 'exit' to quit: ")

    if question.lower() == "exit":
        break

    try:

        answer = agent.ask(question)

        print("\nAnswer:")

        print(answer)

    except Exception as ex:

        print("\nERROR:")

        print(ex)