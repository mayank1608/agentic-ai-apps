from agents.sql_agent import SQLAgent

agent = SQLAgent()

while True:

    question = input(
        "\nAsk Question or type 'exit' to quit: "
    )

    if question.lower() == "exit":
        break

    answer = agent.ask(question)

    print("\nAnswer:")

    print(answer)