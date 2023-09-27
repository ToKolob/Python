
#to make the game more functional I add a loop in the choice, now the game don't stop if the player choose something wrong.

print("\nOnce upon a time there was a character named John, who was in a forest and had to choose which path to take to find a hidden treasure. He came across a fork in the road and had to choose which way to go.")


valid_options = ['right', 'left']
choice1 = ''
while choice1 not in valid_options:
    choice1 = input("\nRIGHT or LEFT? ").lower()
if choice1 == "right":
    print("\nJohn takes the path to the right\nBy following the path to the right, John comes across a lake and must decide whether to swim across it or go around it along the shore.")

    valid_options = ['swims', 'around']
    choice11 = ''
    while choice11 not in valid_options:
        choice11 = input("\nSWIMS or AROUND? ").lower()
    if choice11 == "swims":
        print("\nJohn decides it's better to swim across the lake and manages to make it to the other side. He finds a cave and must decide whether to enter or keep going.")

        valid_options = ['enter', 'keep going']
        choice111 = ''
        while choice111 not in valid_options:
            choice111 = input("\nENTER or KEEP GOING? ").lower()
        if choice111 == "enter":
            print("\nJohn goes into the cave and finds the hidden treasure. He is very happy with the discovery and returns home with the treasure.\n\nHappy End!")
        elif choice111 == "keep going":
            print("\nHe keep going thrght out a very long path but nothing happens, he thinks that the tresure was to see the nature of the florest and return home happy.")
    elif choice11 == "around":
        print("\nJohn is bite by a snake and need to be rescued by an helicopter.")    
elif choice1 == "left":
    print("\nJohn takes the path to the left\nBy following the path to the left, John comes across a mountain and must decide whether to climb it or go around it.")

    valid_options = ['climb', 'around']
    choice12 = ''
    while choice12 not in valid_options:
        choice12 = input("\nCLIMB or AROUND? ").lower()
    if choice12 == "climb":
        print("\nJohn decides it's more exciting to climb the mountain and manages to reach the top. He finds a cave and must decide whether to enter or keep going.")

        valid_options = ['enter', 'keep going']
        choice121 = ''
        while choice121 not in valid_options:
            choice121 = input("\nENTER or KEEP GOING? ").lower()
        if choice121 == "enter":
            print("\nJohn decides to enter in cave, the cave was large humid, he slipped by the entrance and thought the danger is to enter alone in a cave, and moved by his fear give up of find crazy tressures end retorn to his home safe and sound.")
        elif choice121 == "keep going":
            print("\nHe keep going thrght out a very long path but nothing happens, he thinks that the tresure was to see the nature of the mountains and return home happy.")
    elif choice12 == "around":
        print("\nJohn decides to go around the mountain, but for his dispair a big black bear appeared! He must decide to run of fight the bear")

        valid_options = ['fight', 'run']
        choice122 = ''
        while choice122 not in valid_options:
            choice122 = input("\nFIGHT or RUN? ").lower()
        if choice122 == "fight":
            print("\nJohn in the frenezy of the momment to fight the bear and has his life finished by a bear paw.")
        elif choice122 == "run":
            print("\nJohn tried to run and scape, but the bear was too fast and sadly this was the end of our intrept hero...")

        





    