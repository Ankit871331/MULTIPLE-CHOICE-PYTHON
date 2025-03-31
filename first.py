from question import Questions

question_promt = [
    "what color of apple?\n (a)red \n (b)black \n (c)pink \n  (d)non of these \n \n",
    "what color of your ?\n (a)red \n (b)black \n (c)pata nai \n  (d)non of these \n \n",
    "what color of banana?\n (a)red \n (b)yellow \n (c)pink \n  (d)non of these \n \n"
]

questions = [
    Questions(question_promt[0], "a"),
    Questions(question_promt[1], "c"),
    Questions(question_promt[2], "b")
]

def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.promt)
        if answer == q.answer:
            score+= 1
    print("you got "+str((score)) + "/ " + str(len(questions)) + "correct")



run_test(questions)