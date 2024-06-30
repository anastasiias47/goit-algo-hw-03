import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = []
    while len(random_numbers) <= quantity:
        number = random.randint(min, max)
        if number not in random_numbers:
            random_numbers.append(number)

    return sorted(random_numbers)

print(get_numbers_ticket(1, 20,5))
 #asdasdsd-=AO[PDSFODP[S
