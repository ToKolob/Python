def compute_area_square (square_side,rectangle_side=False):
    if rectangle_side == False:
        area = float(square_side) ** 2
    else:
        area = float(square_side)*float(rectangle_side)
    return area

def compute_area_circle (radium):
        circle_area = float(radium)**2 * 3.14159265359
        return circle_area

play_again = '1'
while play_again == '1':

    object_request = ''
    valid_answers = ['1','2','3','4']
    while object_request not in valid_answers and object_request != "4":
        object_request = input("What type of object do you what to calculate area?\n1 - square  \n2 - rectangle   \n3 - circle   \n4 - quit program\n")
    
    if object_request == "1":
        interest_square = input("What is the lenght of the side of the square? ")
        square_area = compute_area_square(interest_square)
        print(f"The area of the square is {square_area}m2\n")

    elif object_request == "2":
        interest_rectangle_side1 = input("What is the lenght of the side of the rectangle?")
        interest_rectangle_side2 = input("What is the lenght of the second side of the rectangle?")
        rectangle_area = compute_area_square(interest_rectangle_side1,interest_rectangle_side2)
        print(f"The area of the rectangle is {rectangle_area}m2\n")
    
    elif object_request == "3":
         radium_interest = input("What is the radium of the circle? ")
         clircle_area = compute_area_circle(radium_interest)
         print(f"The area of the circle is {clircle_area}m2\n")
    
    play_again = ""
    valid_answers = ['1','2']
    while play_again not in valid_answers:
         play_again = input("Do You wanna play again?   \n1 - keep going   \n2 - quit\n")

        
          








