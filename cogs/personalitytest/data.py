import json
import pathlib


class Question:
    def __init__(self, question: str, answers: list['Answer']):
        self.text = question
        self.answers = answers


class Answer:
    def __init__(self, answer: str, natures: dict[str, int]):
        self.text = answer
        self.natures = natures


def load_questions() -> list[Question]:
    quiz_dir = pathlib.Path(__file__).parent / 'quiz'
    with open(quiz_dir / 'questions-en.json') as f:
        data = json.load(f)
    questions = []
    for entry in data:
        answers = [Answer(x['response'], x['scores']) for x in entry['responses']]
        question = Question(entry['title'], answers)
        questions.append(question)
    return questions
