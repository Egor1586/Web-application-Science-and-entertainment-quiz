import openai, dotenv, os

dotenv.load_dotenv()
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRET_KEY)

async def generate_test(topic: str, description:str, count_question: int, aswer_on_question: int):
    """
    функція яка отримує відповідь від штучного інтелекту за допомогою моделі gpt-4o-mini
    """
    promt = "Привіт, створи мені тест простий на тему Python, який включає в себе 5 питань. На кожне питання у чата є відповіді, три які з них - не правильні, а лише одна правильна"
    response = await client_openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{
            "role": "user",
            "content": ''
        }],
    )

    response= {
        "topic": "Основи Python",
        "description": "Тест на базові знання Python для початківців.",
        "questions": [
            {
            "question": "Яка правильна команда для виводу тексту на екран у Python?",
            "options": [
                "echo('Hello World')",
                "console.log('Hello World')",
                "printf('Hello World')",
                "print('Hello World')"
            ],
            "correct_answer": "print('Hello World')"
            },
            {
            "question": "Який тип даних використовується для зберігання цілих чисел у Python?",
            "options": [
                "float",
                "str",
                "bool",
                "int"
            ],
            "correct_answer": "int"
            },
            {
            "question": "Як позначається початок коментаря в Python?",
            "options": [
                "//",
                "<!-- -->",
                "/* */",
                "#"
            ],
            "correct_answer": "#"
            },
            {
            "question": "Який з наведених варіантів створює список у Python?",
            "options": [
                "(1, 2, 3)",
                "{1, 2, 3}",
                "<1, 2, 3>",
                "[1, 2, 3]"
            ],
            "correct_answer": "[1, 2, 3]"
            },
            {
            "question": "Як можна отримати довжину списку у Python?",
            "options": [
                "length(list)",
                "count(list)",
                "size(list)",
                "len(list)"
            ],
            "correct_answer": "len(list)"
            }
        ]
        }
   
    # return response.choices[0].message.content 
    return response


