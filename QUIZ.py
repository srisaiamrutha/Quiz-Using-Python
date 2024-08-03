print("Entering into the game of quiz!")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Sure let's get started :)")
score = 0

answer = input("What does AI stands for? ")
if answer.lower() == "artificial intelligence":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("Who invented C language? ")
if answer.lower() == "dennis ritchie":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does USB stands for? ")
if answer.lower() == "universal serial bus":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does PDF stands for? ")
if answer.lower() == "portable document format":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does LAN stands for? ")
if answer.lower() == "local area network":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("Who is the father of computers? ")
if answer.lower() == "charles babbage":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What was the first computer called? ")
if answer.lower() == "eniac":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/10)*100) + "%")

# Removed the duplicate print statements for incorrect questions