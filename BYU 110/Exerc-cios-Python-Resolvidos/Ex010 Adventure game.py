print("Once upon a time there was a character named John, who was in a forest and had to choose which path to take to find a hidden treasure. He came across a fork in the road and had to choose which way to go.")

choice1 = input("Right or left?").lower()
if choice1 == "right":
    print("\nJohn takes the path to the right\nBy following the path to the right, John comes across a lake and must decide whether to swim across it or go around it along the shore.")
    
    choice11 = input("\nSwims or around").lower()
    if choice11 == "swims":
        print("\nJohn decides it's better to swim across the lake and manages to make it to the other side. He finds a cave and must decide whether to enter or keep going.")
        choice111 = input("\nEnter or keep going").lower()
        if choice111 == "enter":
            print("\nJohn goes into the cave and finds the hidden treasure. He is very happy with the discovery and returns home with the treasure.\n\nHappy End!")
        elif choice111 == "keep going":
            print("\nHe keep going thrght out a very long path but nothing happens, he thinks that the tresure was to see the nature of the florest and return home happy.")
    elif choice11 == "around":
        print("John is bite by a snake and need to be rescued by an helicopter.")    
elif choice1 == "left":
    print("John takes the path to the left\nBy following the path to the left, John comes across a mountain and must decide whether to climb it or go around it.")
    choice12 = input("\nclimb or around?").lower()
    if choice12 == "climb":
        print("John decides it's more exciting to climb the mountain and manages to reach the top. He finds a cave and must decide whether to enter or keep going.")
        choice121 = input("\nEnter or keep going?").lower()
        if choice121 == "enter":
            print("John decides to enter in cave, the cave was large humid, he slipped by the entrance and thought the danger is to enter alone in a cave, and moved by his fear give up of find crazy tressures end retorn to his home safe and sound.")
        elif choice121 == "keep going":
            print("\nHe keep going thrght out a very long path but nothing happens, he thinks that the tresure was to see the nature of the mountains and return home happy.")
    elif choice12 == "around":
        print("\nJohn decides to go around the mountain, but for his dispair a big black bear appeared! He must decide to run of fight the bear")
        choice122 = input("\nFight or run?").lower()
        if choice122 == "fight":
            print("John in the frenezy of the momment to fight the bear and has his life finished by a bear paw.")
        elif choice122 == "run":
            print("John tried to run and scape, but the bear was too fast and sadly this was the end of our intrept hero...")

        





    