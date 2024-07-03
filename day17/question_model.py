class Question:
    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer
        
        
    def __str__(self) -> str:
        return f'{self.text} {self.answer}'