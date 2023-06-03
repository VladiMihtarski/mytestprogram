# print("Welcom to my computer quiz!")
#
# playing = input("Do you want to play? ")
#
# if playing.lower() != "yes":
#     quit()
#
# print("Okay! Let`s play:) ")
# score = 0
#
# answer = input("What does CPU stand for? ")
# if answer.lower() == "central processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")
#
# answer = input("What does GPU stand for? ")
# if answer.lower() == "graphics processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")
#
# answer = input("What does RAM stand for? ")
# if answer.lower() == "random access memory":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")
#
# answer = input("What does PSU stand for? ")
# if answer.lower() == "power supply":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")
# print("You got " + str(score)+" questions correct! ")
# print("You got " + str((score/ 4 ) * 100)+ "%.")

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:) ")
score = 0

questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply")
]

for question, correct_answer in questions:
    answer = input(question)
    if answer.lower() == correct_answer:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / len(questions)) * 100) + "%.")
