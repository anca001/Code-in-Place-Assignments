def main():
    # TODO write your solution here
    sequence_number = 1
    print("Enter a sequence of non-decreasing numbers.")
    previous_number = float(input("Enter num: ")) 
    current_number = float(input("Enter num: ")) 

    while previous_number <= current_number: 
        sequence_number += 1
        previous_number = current_number
        current_number = float(input("Enter num: ")) 

    print("Thanks for playing") 
    print("Sequence length: " + str(sequence_number))


if __name__ == "__main__":
    main()
