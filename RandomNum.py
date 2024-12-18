import random
from collections import Counter

count = Counter()
previous_set = None  

def gen_set(items=None):
    global count, previous_set

    if items is None:
        while True:
            user_input = input("Enter exactly 10 numbers or letters separated by commas: ")
            items = [item.strip() for item in user_input.split(",")]

            if len(items) != 10:  # adjust the required length of items here
                print("Please enter exactly 10 items.")
                continue

            processed_items = []
            for item in items:
                if item.isdigit():  
                    processed_items.append(int(item))
                elif item.isalpha() and len(item) == 1:  
                    processed_items.append(item.upper())
                else:
                    print("Invalid input. Please enter only numbers or single letters.")
                    break
            else:
                items = processed_items
                break

    def random_sample(items, k=4):  #  change the number of selected items here
        weights = [1 / (count[item] + 1) for item in items]
        chosen = random.choices(items, weights=weights, k=k)
        count.update(chosen)
        return chosen

    selected = []
    while len(selected) < 4:
        candidate = random_sample(items, k=1)[0]
        if candidate not in selected:
            selected.append(candidate)

    numbers = [item for item in items if isinstance(item, int)]
    avg_num = sum(numbers) / len(numbers) if numbers else 50 

    rand_items = set()
    while len(rand_items) < 6:  # change the number of random items here
        new_item = int(avg_num + random.uniform(-20, 20)) if random.random() > 0.5 else chr(random.randint(65, 90))
        if new_item not in rand_items and count[new_item] == 0:  
            rand_items.add(new_item)

    new_set = list(set(selected + list(rand_items)))
    while len(new_set) < 10:  # adjust the final set size here
        filler = random.randint(1, 100) if random.random() > 0.5 else chr(random.randint(65, 90))
        if filler not in new_set and count[filler] == 0:  
            new_set.append(filler)
    random.shuffle(new_set)

    previous_set = new_set

    print("New set:", new_set)
    print("-" * 50)

while True:
    gen_set(previous_set)

    while True:
        repeat = input("Do you want to repeat with the previous set? (Yes/No): ").strip().lower()

        if repeat in ['yes', 'y']:
            break  
        elif repeat in ['no', 'n']:
            print("End of Program")
            exit()
        else:
            print("Invalid input. Please respond with 'Yes' or 'No'.")

# 4, 8, 15, 16, 23, a, b, C, X, y
