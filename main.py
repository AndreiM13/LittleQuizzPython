from Question import Question

while True:
    question_prompts = ["What color have apples?\n(a)Red/green\n(b)Purpule\n(c)Blue\n\n",
                        "What color have banana?\n(a)Red/green\n(b)Purpule\n(c)Yellow\n\n",
                        "What color have grapes?\n(a)green\n(b)Purpule\n(c)Blue\n\n"
                        ]
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "a")
    ]


    def ready_s():
        while True:
            c = input("Are you ready?:")
            if c == "yes":
                run_test(questions)
            else:
                print("Bye")


    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("You got" + " " + str(score) + "/" + str(len(questions)) + " " + "Corect")


    ready_s()




