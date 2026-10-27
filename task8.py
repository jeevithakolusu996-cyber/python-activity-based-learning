
def hollow_diamond(n):
    """Print a hollow diamond with 2*n - 1 rows."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        print("Error: Size must be a positive integer.")
        return

    for i in range(1, 2 * n):
        level = i if i <= n else 2 * n - i
        spaces = n - level

        if level == 1:
            print(" " * spaces + "1")
        else:
            inner_spaces = 2 * level - 3
            print(
                " " * spaces
                + str(level)
                + " " * inner_spaces
                + str(level)
            )


def symmetric_number_pattern(n):
    """Print ascending and descending numbers symmetrically."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        print("Error: Size must be a positive integer.")
        return

    for i in range(1, n + 1):
        left = list(range(1, i + 1))
        right = list(range(i - 1, 0, -1))
        row = left + right
        print(" " * (n - i) + " ".join(map(str, row)))


def main():
    print("Numeric Pattern Generator")
    print("1. Hollow Diamond")
    print("2. Symmetric Number Pattern")

    try:
        choice = int(input("Choose pattern (1 or 2): "))
        n = int(input("Enter pattern size (positive integer): "))

        if n < 1:
            print("Error: Dimension must be at least 1.")
            return

        if n > 50:
            print("Error: Maximum supported size is 50.")
            return

        if choice == 1:
            hollow_diamond(n)
        elif choice == 2:
            symmetric_number_pattern(n)
        else:
            print("Error: Choose option 1 or 2.")

    except ValueError:
        print("Error: Enter valid whole numbers only.")


if __name__ == "__main__":
    main()
