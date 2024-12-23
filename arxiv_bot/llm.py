from openai import OpenAI

class LLMClient:
    def __init__(self, system_prompt=None ,model_name='gpt-4o-mini'):
        self.llm = OpenAI()
        self.model_name = model_name
        self.history = []
        if system_prompt is not None:
            self.history.append({
                'role': 'system',
                'content': system_prompt,
            })

    def singleGeneration(self, prompt):
        result = self.llm.chat.completions.create(
            model=self.model_name,
            messages=[
                { 'role': 'user', 'content': prompt},
            ],
        )
        return result.choices[0].message.content
    
    def chat(self, prompt):
        self.history.append({
            'role': 'user',
            'content': prompt,
        })
        result = self.llm.chat.completions.create(
            model=self.model_name,
            messages=self.history,
        )

        response = result.choices[0].message.content
        self.history.append({
            'role': 'assistant',
            'content': response,
        })

        return response
