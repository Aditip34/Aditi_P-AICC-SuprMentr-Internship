name = input()
age = int(input())
hobby = input()

if age < 13:
    cat = "Child"
elif age < 20:
    cat = "Teen"
elif age < 60:
    cat = "Adult"
else:
    cat = "Senior"

print(f"{name} is an {cat} who likes {hobby}")