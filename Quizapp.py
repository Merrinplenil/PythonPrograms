
# import time
# mark = 0
# print("Quick Python Quiz\nThere will be 5 MCQ Questions with 1 point each.Total time 50 Seconds")
# name=input("Enter your name")
# if name:
#     input(f"{name} Are You Ready? Press Enter")
#     start=time.time()
#     print(start)
#     print("Quiz ON")
#     print("1. What is the correct file extension for Python files?")
#     print("\na.txt\nb.png\nc.py")
#     a1=input("Answer: ").lower()
#     if a1=='c':
#         mark=mark+1
#         print("Correct Answer")
#     else:
#         print("Wrong")
#     print("\n2. Which of these data types is immutable in Python?")
#     print("\na.List\nb.Tuple\nc.Set")
#     a1=input("Answer:").lower()
#     if a1=='b':
#         mark=mark+1
#         print("Correct Answer")
#     else:
#         print("Wrong")
#     print("\n 3. Which of the following is a valid variable name in Python?")
#     print("\na.1name\nb.@name\nc.name")
#     a1=input("Answer:").lower()
#     if a1=='c':
#         mark=mark+1
#         print("Correct Answer")
#     else:
#         print("Wrong")
#     print("\n 4. Which of the following is not a keyword in Python?")
#     print("\na.define\nb.def\nc.print")
#     a1=input("Answer:").lower()
#     if a1=='a':
#         mark=mark+1
#         print("Correct Answer")
#     else:
#         print("Wrong")
#     print("\n 5. What is the output of: print(2 ** 3)?")
#     print("\na.6\nb.5\nc.8")
#     a1=input("Answer:").lower()
#     if a1=='c':
#         mark=mark+1
#         print("Correct Answer")
#     else:
#         print("Wrong")
#     end=time.time()
#     difference = end-start
#     print(f"\nTime taken: {difference} seconds")
#     if difference <50:
#         print(f"Your total Score is {mark}")
#     else:
#         print("Time Out ...You failed")

import time

def MCQ(question, options, correct_answer):
    print(f"\n{question}")
    for option in options:
        print(option)
    answer = input("Answer: ").lower()
    if answer == correct_answer:
        print("Correct Answer")
        return 1
    else:
        print("Wrong")
        return 0
def quiz_start():
    mark = 0
    print("Quick Python Quiz\nThere will be 5 MCQ Questions with 1 point each. Total time 50 Seconds")
    name = input("Enter your name: ")
    
    if name:
        input(f"{name} Are You Ready? Press Enter")
        start = time.time()
        print("Quiz ON")
        
        # Question 1
        mark += MCQ("1. What is the correct file extension for Python files?", 
                           ["a.txt", "b.png", "c.py"], "c")
        
        # Question 2
        mark += MCQ("2. Which of these data types is immutable in Python?", 
                           ["a.List", "b.Tuple", "c.Set"], "b")
        
        # Question 3
        mark += MCQ("3. Which of the following is a valid variable name in Python?", 
                           ["a.1name", "b.@name", "c.name"], "c")
        
        # Question 4
        mark += MCQ("4. Which of the following is not a keyword in Python?", 
                           ["a.define", "b.def", "c.print"], "a")
        
        # Question 5
        mark += MCQ("5. What is the output of: print(2 ** 3)?", 
                           ["a.6", "b.5", "c.8"], "c")
        
        end = time.time()
        difference = end - start
        print(f"\nTime taken: {difference} seconds")
        if difference < 50:
            print(f"Your total Score is {mark}")
        else:
            print("Time Out ...You failed")

# Start the quiz
quiz_start()
