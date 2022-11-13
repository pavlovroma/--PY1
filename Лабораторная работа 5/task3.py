def get_unique_list_numbers() -> list[int]:
    from random import randint

    return [randint(-10, 10) for _ in range(15)]

print(get_unique_list_numbers())


