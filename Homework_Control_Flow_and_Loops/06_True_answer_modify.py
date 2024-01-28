answer = int(input("Please answer a question - how year old am I? (hint between 20 and 40): "))

while answer != 39:
    answer = int(input("Wrong answer, please try again: "))
if answer == 39:
    print("Congratulation, True answer.")
    print("Next question")

answer = input("in which city live am I? (hint - one of the 5 biggest cities in Bulgaria): ")
while answer != "Plovdiv":
    answer = input("Wrong answer, please try again: ")
if answer == "Plovdiv":
    print("Congratulation, True answer.")
    print("Next question")

answer = input("Am i hungry? (hint - Yes, No, Maybe): ")
while answer != "Yes":
    answer = input("Wrong answer, please try again: ")
if answer == "Yes":
    print("Congratulation, True answer.")

