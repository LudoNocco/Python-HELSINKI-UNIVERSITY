def read_input(prompt: str, lower_bound: int, upper_bound: int) -> int:
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if lower_bound <= number <= upper_bound:
                return number
            else:
                print(f"You must type in an integer between {lower_bound} and {upper_bound}")
        except ValueError:
            print(f"You must type in an integer between {lower_bound} and {upper_bound}")
