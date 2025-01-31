from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, background=THEME_COLOR)
        
        self.score_lable = Label(text="Score: 0",fg="white", font=("Ariel", 20, "italic"), background=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)
        
        self.canvas  = Canvas(height=250, width=300, background='white')
        self.question_text = self.canvas.create_text(
            150, 125, 
            width=280,
            text="Hello", 
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        
        self.right_photo = PhotoImage(file="images/true.png")
        self.wrong_photo = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.right_photo, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=self.wrong_photo, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        