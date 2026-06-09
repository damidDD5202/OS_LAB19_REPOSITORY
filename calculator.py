def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def main() -> None:
    print("Simple calculator demo:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"7 - 4 = {subtract(7, 4)}")
    print(f"6 * 5 = {multiply(6, 5)}")
    print(f"8 / 2 = {divide(8, 2)}")


if __name__ == "__main__":
    main()
