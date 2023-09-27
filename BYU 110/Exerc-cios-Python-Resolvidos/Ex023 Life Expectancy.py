with open ("E:\My Drive\Programação\Python\BYU 110\life-expectancy.csv") as database:
    max_life_expectancy = 0
    min_life_expectancy = 999
    country_max = ""
    country_min = ""
    date = ""
    
    
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
    
    
    
while 1 != 0:

    date_request = input("Enter the year of interest: ")

    max_life_expectancy = 0
    min_life_expectancy = 999
    country_max = ""
    country_min = ""
    date = ""
    averenge = 0
    n = 0

    with open ("E:\My Drive\Programação\Python\BYU 110\life-expectancy.csv") as database:
        for line in database:
            parts = line.split(",")        
            years = parts[3]
            years = years.strip()
            date = parts[2]
            date = date.strip()
            
            if date == date_request:

                try:
                    years = float(years)
                    averenge += years
                    n += 1

                    if years > max_life_expectancy:
                        max_life_expectancy = years
                        country_max = parts[0]

                    if years < min_life_expectancy:
                        min_life_expectancy = years
                        country_min = parts[0]

                except ValueError:
                    continue
        averenge = averenge/n    
        print (f"For the year {date_request}:")
        print (f"The average life expectancy across all countries was {averenge:.2f}")
        print (f"The max life expectancy was in {country_max} with {max_life_expectancy}")
        print (f"The min life expectancy was in {country_min} with {min_life_expectancy}\n\n")


