print("Hello, welcome to my quiz about AI!")

want_to_play = (input("Do you want to play? (yes/no) "))

if want_to_play.lower() != 'yes':
    quit()


print("Okay! Let's start then! :) ")
score = 0

answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ML stand for? ")
if answer.lower() == "machine learning":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does NLP stand for? ")
if answer.lower() == "natural language processing":
    print("Correct!")
    score += 3
else:
    print("Incorrect!")

answer = input("What does DS stand for? ")
if answer.lower() == "data science":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

print("Congratulaions, your score is " + str(score) +"points")

print("You got " +str((score / 7)*100) + "%")









