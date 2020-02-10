print("Enter the number of choices:")
n = int(input())
print("Enter your choices")
choices = []
choice_score = []
final_dec = {}
for i in range(0, n):
    choices.append(input())
print("Good, now input your parameters and their corresponding weightage. Enter exit once done!")
parameters = {}
while True:
    parameter = input()
    if parameter == "exit":
        break
    weightage = int(input())
    parameters[parameter] = weightage
print("Let's begin the decision making..Enter your score for each parameter")
for choice in choices:
    choice_score = []
    print(choice + ": ")
    score = []
    for parameter in parameters:
        print(parameter + " :")
        score = int(input())
        choice_score.append(parameters[parameter] * score)
    print("choice_score: ", choice_score)
    final_dec[choice] = sum(choice_score)
print("Your Results: ", final_dec)





