def user_name (name: str) -> str:
    import random
    reverse = name[::-1]
    random_int = random.randint(0, 9)
    output = reverse + str(random_int)
    return output

def sort_names_cheat (names: list) -> list:
    return sorted(names)

def sort_names (names: list) -> list:
    # sort names based on length
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if len(names[i]) > len(names[j]):
                names[i], names[j] = names[j], names[i]
    return names

if __name__ == "__main__":
    input_name = "richard" #input("Enter your name: ")
    print(user_name(input_name))

    print(sort_names([ "Peter", "Jon", "Andrew"]))


