import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(verbose=True)


class BaseAgent:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    
    async def llm_call(self, prompt: str, text: str = "") -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
