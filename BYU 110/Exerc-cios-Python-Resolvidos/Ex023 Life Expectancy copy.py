#I add a loop in the program to reopen the file and find other numbers, also I add a test of validation to the user input a number inside the range, however I should have create a list with the valid dates insted.

with open ("E:\My Drive\Programação\Python\BYU 110\life-expectancy.csv") as database:
    max_life_expectancy = 0
    min_life_expectancy = 999
    country_max = ""
    country_min = ""
    date = ""
    max_valid_date = 0
    min_valid_date =9999
    
    
    for line in database:
        parts = line.split(",")
        years = parts[3]
        years = years.strip()
        date = parts[2]
        date = date.strip()
        try:
            years = float(years)
            date = int(date)

            if date > max_valid_date:
                max_valid_date = date
            if date < min_valid_date:
                min_valid_date = date            


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
    print (f"In the range of year {min_valid_date} to year {max_valid_date}.\nThe highest life expectancy was in {country_max}, with {max_life_expectancy}, on {date_max}, \nand the lowest was in {country_min}, with {min_life_expectancy}, on {date_min}\n")
    
    
    
while 1 != 0:
    date_request = 9999
    while date_request > max_valid_date or date_request < min_valid_date:
        date_request = input(f"Enter the year of interest({min_valid_date} to {max_valid_date}): ")
        date_request = int(date_request)
    
    date_request = str(date_request)
    max_life_expectancy = 0
    min_life_expectancy = 999
    country_max = ""
    country_min = ""
    date = "a"
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


