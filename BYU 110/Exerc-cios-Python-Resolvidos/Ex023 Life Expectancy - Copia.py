with open ("E:\My Drive\Programação\Python\BYU 110\life-expectancy.csv") as database:
    max_life_expectancy = 0
    min_life_expectancy = 999
    country_max = ""
    country_min = ""
    date_max = ""
    date_min = ""
    for line in database:
        parts = line.split(",")
        years = parts[3]
        years = years.strip()
        try:
            years = float(years)
            if years > max_life_expectancy:
                max_life_expectancy = years
                country_max = parts[0]
                date_max = parts[2]
            if years < min_life_expectancy:
                min_life_expectancy = years
                country_min = parts[0]
                date_min = parts[2]
        except ValueError:
            continue
    print (f"The highest life expectancy was in {country_max}, with {max_life_expectancy}, on {date_max}, and the lowest was in {country_min}, with {min_life_expectancy}, on {date_min}")

    print (line)

    request_date = int(input("Which year do you wanna see?"))
    max_life_expectancy = 0
    min_life_expectancy = 999
    for line in database:
        parts = line.split(",")
        years = parts[3]
        years = years.strip()
        if request_date == parts[2]:
            try:
                years = float(years)
                if years > max_life_expectancy:
                    max_life_expectancy = years
                if years < min_life_expectancy:
                    min_life_expectancy = years
            except ValueError:
                continue
        
    print ("For the year 1959:")
    print (f"The average life expectancy across all countries was {0}")
    print (f"The max life expectancy was in ___ with {max_life_expectancy}")
    print (f"The min life expectancy was in ___ with {min_life_expectancy}")


