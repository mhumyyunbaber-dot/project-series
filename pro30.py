import random
def flashcard():
    print("Welcome to Flash Card App")
    flashcards={
        "What is the capital of Pakistan?":"Islamabad",
        "what is 2+2?":"4",
        "Python is keyword of Function?":"def",
        "Speed formula?":"distance/time"
    }
    questions=list(flashcards.keys())
    random.shuffle(questions)
    
    for question in questions:
        print(f"Question: {question}")
        user_answer = input("what is Your answer: ").strip().lower()
        
        if user_answer == flashcards[question].lower():
            print("Correct")
        
        else:
            print(f"Wrong! The answer is: {flashcards[question]}")
    print("Flash Card session complete!")
flashcard()