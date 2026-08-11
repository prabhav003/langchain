from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = '''
import random
import math


def generate_number():
    return random.randint(1, 100)


class Calculator:

    def __init__(self, name):
        self.name = name

    def square(self, number):
        return math.pow(number, 2)

    def cube(self, number):
        return number ** 3


def show_result(calculator, number):
    print(f"Square: {calculator.square(number)}")
    print(f"Cube: {calculator.cube(number)}")


def main():
    calculator = Calculator("Demo Calculator")
    number = generate_number()

    show_result(calculator, number)


if __name__ == "__main__":
    main()
'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])

print(chunks[1])