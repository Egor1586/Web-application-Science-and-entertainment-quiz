import openai, dotenv, os

dotenv.load_dotenv()
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRET_KEY)

async def generate_test(topic: str, count_question: int, nswer_on_question: int):
    """
    функція яка отримує відповідь від штучного інтелекту за допомогою моделі gpt-4o-mini
    """
    promt = ""
    response = await client_openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{
            "role": "user",
            "content": ''
        }],
    )
   
    return response.choices[0].message.content 