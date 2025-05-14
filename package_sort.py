def sort(width: int, height: int, length: int, mass: int) -> str:
    if min(length, width, height, mass) < 0:
        return "Error negative input"

    vol = length * width * height
    bulky = False
    heavy = False

    if vol >= 1000000 or max(length, width, height) >= 150:
        bulky = True
    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"

def tests():
    failed = False
    if sort(1, 1, 1, 1) != "STANDARD": failed = True
    if sort(100, 100, 100, 1) == "SPECIAL": failed = True
    if sort(149, 10, 10, 20) == "SPECIAL": failed = True
    if sort(1, 1, 151, 25) == "REJECTED": failed = True
    if sort(150, 1, 1, 1) == "SPECIAL": failed = True
    if sort(10, 10, 10, 20) == "SPECIAL": failed = True
    if sort(10, 10, 10, 19) == "STANDARD": failed = True
    if sort(10, 10, 10, 21) == "SPECIAL": failed = True
    
    if failed:
        return "failure"
    return "success"
        


if __name__ == "__main__":
    tests()
