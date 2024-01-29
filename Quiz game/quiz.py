def quiz_game():
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("What is the largest mammal?", "Blue whale"),
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the powerhouse of the cell?", "Mitochondria"),
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
        ("What is the tallest land animal?", "Giraffe"),
        ("Which country is known as the Land of the Rising Sun?", "Japan"),
        ("What is the capital of Australia?", "Canberra")
    ]

    score = 0

    for question, correct_answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: {}".format(correct_answer))

    print("You got {} out of {} questions correct.".format(score, len(questions)))


quiz_game()