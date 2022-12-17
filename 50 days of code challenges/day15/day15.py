def same_in_reverse(input:str)-> bool:
    if input[::-1] == input:
        is_palindrome = True
    else:     
        is_palindrome = False
    return is_palindrome

def your_age(name:str, age:int = 0) -> str:
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    if name.lower() in names_age:
        age = names_age[name.lower()]
    elif age != 0:
        names_age[name.lower()] = age
    else:
        raise ValueError("Name not found")
    return f'Hi, {name}, you are {age} years old.'

if __name__ == "__main__":
    user = input("What is your name? ")
    try: 
        answer = your_age(user)
        print(answer)
    except ValueError as e:
        if e.args[0] == 'Name not found':
            age = int(input("What is your age? "))
            answer = your_age(user, age)
            print(answer)
