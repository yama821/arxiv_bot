from arxiv_bot.llm import LLMClient


def main():
    llm = LLMClient()
    res = llm.singleGeneration("こんにちは")
    print(res)

if __name__ == "__main__":
    main()
