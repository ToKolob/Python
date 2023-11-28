def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print(f"type of list: {type(fruit_list)}")

    # Sort the list.
    revest_list = fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Add a fruit to the end of the list.
    fruit_list.append("orange")

    print(f"adding 'orange': {fruit_list}")
    print(f"type of: {type(fruit_list)}")

    # Remove a fruit from the list.
    fruit_list.remove("banana")
    print(f"removing 'banana': {fruit_list}")

    # Pop the last fruit.
    last_fruit = fruit_list.pop()
    print(f"popping last fruit: {last_fruit}")
    print(f"popping last fruit: {fruit_list}")

    # sort the list
    fruit_list.sort() 
    print(f"sorted: {fruit_list}")

    # clear the list
    fruit_list.clear()
    print(f"clearing: {fruit_list}")

if __name__ == "__main__":
    main()