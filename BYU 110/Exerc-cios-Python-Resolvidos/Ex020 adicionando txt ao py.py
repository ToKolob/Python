with open ("books.txt") as bok:
    for name in bok:
        name_clean = name.strip()
        print(name_clean)