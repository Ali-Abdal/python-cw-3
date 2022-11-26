# part 1

favorite_animals = ["Cat", "Seal", "Horse", "Penguin"]

print(favorite_animals)

print(favorite_animals[2])

favorite_animals.remove("Horse")

# part 2

favorite_animals.append("Bee")

for animal in favorite_animals:
    print(f"I love {animal}")

# part 3

numbers = [2, 4, 5, 6, 9]

numbers_sum = 0

for number in numbers:
    numbers_sum += number

print(numbers_sum)