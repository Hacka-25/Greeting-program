# Quiz data: each question is a dictionary with question, options, and answer
quiz_questions =[
    {
        "question": "What does the 'len()' function do in Python?",
        "options": ["A. Finds length", "B. Adds numbers", "C. Converts to string", "D. Loops ththrough items"],
        "answer": "A"
    },
    {
        "question": "Which movie was produced first under Phil It Productions?",
        "options": ["A. Grand Little Lie", "B. Click Click Bang", "C. Makosa ni Yangu", "D. NAirobi Half Life"],
        "answer": "A"

    },
    {
        "question": "What Python Data Type is immutable?",
        "options": ["A. Lists", "B. Sets", "C. Strings", "D. Tuples"],
         "answer": "D"
           
           },
           {
               "question" : "Who plays Kev in Click Click Bang?",
               "options":["A. Isaboke Nyakundi", "B. Abel Mutua", "C. Philip Karanja", "D. Basil Mungai"],
               "answer":"D"

           },
]
def run_quiz():
    score = 0 #initialize score

    for i, question_data in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {i}: {question_data['question']}")
        for option in question_data["options"]:
            print(option)

        answer = input("Your answer (A, B, C, D): ").strip().upper()

        if answer == question_data["answer"]:
            print("✅ Correct!")
            score +=1
                
        else:
            print(f"❌ Wrong! The correct answer was {question_data['answer']}")

    print(f"\n🏴 Quiz Complete! You scored {score} out of {len(quiz_questions)}🏆")


def start_quiz():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break
        

#Start the quiz
start_quiz()


