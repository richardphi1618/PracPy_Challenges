import emoji

def your_vat(msrp: float, vat: float) -> float:
    return round((msrp*(vat/100))+msrp ,2)

def python_snakes(input: int = 1) -> None:
    for idx, i in enumerate(range(input)):
        print(emoji.emojize(':snake: '*(idx+1)))
    return None


if __name__ == "__main__":
    
    pass
