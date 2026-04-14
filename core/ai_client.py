from groq import Groq
from core.config import GROQ_API_KEY, MODEL_NAME, SYSTEM_PROMPT

class AIClient:
    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found. Check your .env file.")
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = MODEL_NAME
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=0.4,
            max_completion_tokens=2048,
            reasoning_effort="none"  # qwen/qwen3-32b supports this on Groq
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def clear_memory(self):
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def get_history(self):
        return self.messages
