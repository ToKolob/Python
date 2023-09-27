def main():
    # Get the first odometer reading from the user
    odometer_miles1 = get_odometer_reading('Enter the first odometer reading (miles):')

    # Get the second odometer reading from the user
    odometer_miles2 = get_odometer_reading('Enter the second odometer reading (miles):')

    # Get the fuel amount from the user
    fuel_amount_gallons = get_fuel_amount('Enter the amount of fuel used (gallons):')

    # Calculate the miles per gallon
    mpg = calculate_mpg(odometer_miles1, odometer_miles2, fuel_amount_gallons)

    # Calculate the liters per 100 kilometers
    lp100k = calculate_lp100k(mpg)

    # Display the results for the user to see.
    print(f'{mpg} miles per gallon\n{lp100k} liters per 100 kilometers')
    


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end_miles - start_miles) / amount_gallons
    


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.214/mpg


# Call the main function so that
# this program will start executing.
main()
