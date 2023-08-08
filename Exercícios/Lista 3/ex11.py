def is_sorted(list):
    """Returns True if the numbers of a given
    list are in order."""
    previous_number = int(list[0])
    
    for i, number in enumerate(list):
        if i == 0:
            continue
        elif int(number) != previous_number + 1:
            return False

        previous_number = int(number)

    return True

def main():
    number_sequence = input().split()
    print(is_sorted(number_sequence))

main()