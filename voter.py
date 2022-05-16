voter = True

while voter:
    print("Are you a US Citizen?")
    ans = input("Yes or no: ")
    if ans == "yes":
        age = int(input("State your age: "))
        if age >= 18:
            print("You are elgible to vote.")
        elif age < 18:
            print("You must be 18 or older to vote.")
    else:
        print("you are not eligible to vote.")
    