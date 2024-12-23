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
    
    def summarize(self, text):
        prompt = f"""次の文章を日本語で要約してください。
# 制約
* 箇条書きで3項目以内にまとめること
* 専門用語は英語のまま用いること
* 簡潔にすること

# 文章
{text}"""
        return self.singleGeneration(prompt)
