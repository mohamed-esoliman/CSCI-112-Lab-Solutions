from my_priorityQueue import PriorityQueue


def briberyGame():
    bribery = PriorityQueue()
    while True:
        response = input("How much you got? (enter 'done' to finish)")
        if response == "done":
            print("Program finished.")
            break
        try:
            amount = float(response)
            reversedPosition = bribery.push(amount)
            if (amount == 0) or (reversedPosition == 0 and len(bribery) > 1):
                print("Got to the end of the queue. Loser!")
            else:
                print(
                    f"Excellent! You are now in position #{len(bribery) - reversedPosition} in the queue."
                )

        except ValueError:
            print("Please enter a number.")
            continue


def main():
    briberyGame()


if __name__ == "__main__":
    main()
