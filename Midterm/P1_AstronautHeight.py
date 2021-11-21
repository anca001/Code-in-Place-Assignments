def main():
    # TODO write your solution here
    MIN_HEIGHT = 1.6
    MAX_HEIGHT = 1.9

    user_input = int(input("Enter your height in meters: "))
    if 1.6 <= user_input <= 1.9:
        print("Correct height to be an astronaut")
        
    elif user_input < 1.6:
        print("Below minimum astronaut height")

    elif user_input > 1.9:
        print("Above maximum astronaut height")


if __name__ == "__main__":
    main()
