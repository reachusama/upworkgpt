from src.inference import setup
import textwrap


def main():
    chain = setup(docs_path="resources/data")
    q = "Describe your purpose and background knowledge"

    while not q.lower() == "quit":
        response = chain({'query': q})
        print(textwrap.fill(response['result'], width=100))
        q = input("What is your query? >> ")


if __name__ == '__main__':
    main()
