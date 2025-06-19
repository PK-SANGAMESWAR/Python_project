#list of questions
#store the answer
#randomly pick the questions
#ask the questions
#check if they are correct
#keep track of the score
#update the score

import random

questions = {
    "What is Python?": "Python is a high-level, interpreted, general-purpose programming language known for its simplicity and readability.",
    
    "What is a dictionary in Python?": "A dictionary is a collection of key-value pairs enclosed in curly braces, e.g., {'name': 'John', 'age': 25}.",
    
    "How do you create a function in Python?": "Use the def keyword. Example: def greet(): print('Hello!')",
    
    "What is the difference between a list and a tuple?": "A list is mutable (can be changed), whereas a tuple is immutable (cannot be changed).",
    
    "What does the len() function do?": "It returns the number of items in an object (like a list, string, tuple, etc.).",
    
    "What is the use of 'if __name__ == \"__main__\"' in Python?": "It ensures that code runs only when the file is executed directly, not when imported as a module.",
    
    "How do you handle exceptions in Python?": "Using try, except, else, and finally blocks.",
    
    "What is a lambda function?": "A small anonymous function defined using the lambda keyword. Example: lambda x: x * 2",
    
    "What does the 'strip()' function do?": "It removes leading and trailing whitespace from a string.",
    
    "How do you add an element to a list?": "Use the append() method. Example: my_list.append(10)",
    
    "How do you loop through a dictionary?": "Use for key, value in dict.items():",
    
    "What are Python’s data types?": "Common types include int, float, str, list, tuple, dict, set, bool, NoneType.",
    
    "How do you import a module in Python?": "Use the import keyword. Example: import math",
    
    "What is the difference between 'is' and '=='?": "'==' checks for value equality, 'is' checks for identity (same memory location).",
    
    "How do you read user input in Python?": "Use the input() function. Example: name = input('Enter your name: ')",
}


def python_trivia_game():
    questions_list=list(questions.keys())
    total_questions=5
    score=0

    selected_questions=random.sample(questions_list,total_questions)

    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer=input("Your answer: ").lower().strip()

        correct_answer=questions[question]

        if user_answer==correct_answer.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")

    print(f"Game Over! Your final score is {score}/{total_questions}")
    


if __name__ == "__main__":
    python_trivia_game()


