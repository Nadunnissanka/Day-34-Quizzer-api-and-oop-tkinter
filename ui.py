from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 14))
        self.score_label.config(bg=THEME_COLOR, fg="#ffffff", highlightthickness=0, padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="question text here!", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.config(bg="#ffffff", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#ffffff", highlightthickness=0)
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="#77dd77", highlightthickness=0)
        else:
            self.canvas.config(bg="#ff6961", highlightthickness=0)
        self.window.after(1000, self.get_next_question)
