import random 
from functools import reduce


QuestionInfo = tuple[int, str, int, int]

class MathWorksheetGenerator:
    """class for generating math worksheet of specified size and main_type"""
    def __init__(self, type_: str, max_number: int):
        self.main_type = type_
        self.max_number = max_number

    # From https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a
    # -number-in-python
    def factors(self, n: int):
        return set(reduce(list.__add__,
                          ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    def division_helper(self, num) -> list[int, int, int]:
        # prevent num = 0 or divisor = 1 or divisor = dividend
        factor = 1
        while not num or factor == 1 or factor == num:
            num = random.randint(0, self.max_number)
        # pick a factor of num; answer will always be an integer
            if num:
                factor = random.sample(self.factors(num), 1)[0]
        answer = int(num / factor)
        return [num, factor, answer]

    def generate_question(self) -> QuestionInfo:
        """Generates each question and calculate the answer depending on the type_ in a list
        To keep it simple, number is generated randomly within the range of 0 to 100
        :return:  list of value1, main_type, value2, and answer for the generated question
        """
        num_1 = random.randint(0, self.max_number)
        num_2 = random.randint(0, self.max_number)
        if self.main_type == 'mix':
            current_type = random.choice(['+', '-', 'x', '/'])
        else:
            current_type = self.main_type

        if current_type == '+':
            answer = num_1 + num_2
        elif current_type == '-':
            #  avoid having a negative answer which is an advanced concept
            num_1, num_2 = sorted((num_1, num_2), reverse=True)
            answer = num_1 - num_2
        elif current_type == 'x':
            answer = num_1 * num_2
        elif current_type == '/':
            num_1, num_2, answer = self.division_helper(num_1)

        else:
            raise RuntimeError(f'Question main_type {current_type} not supported')
        return num_1, current_type, num_2, answer

    def get_list_of_questions(self, question_count: int) -> list[QuestionInfo]:
        """Generate all the questions for the worksheet in a list. Initially trying for unique questions, but
        allowing duplicates if needed (e.g. asking for 80 addition problems with max size 3 requires duplication)
        :return: list of questions
        """
        questions = []
        duplicates = 0
        while len(questions) < question_count:
            new_question = self.generate_question()
            if new_question not in questions or duplicates >= 10:
                questions.append(new_question)
            else:
                duplicates += 1
        return questions

if __name__ == "__main__":
    generator = MathWorksheetGenerator("-", 999)
    print(generator.get_list_of_questions(2))