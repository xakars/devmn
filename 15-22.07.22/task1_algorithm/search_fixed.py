from random import sample


def get_number_from_user():
    while True:
        try:
            user_number = int(input("\nPick a number between 0-100: "))
            if user_number < 0 or user_number > 100:
                print("Number isn't range between 0-100")
                continue
            break
        except ValueError:
            print("That's not a number.\n")
    return user_number


def get_random_int_list():
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))
    return rand_list

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    user_input = get_number_from_user()
    rand_list = get_random_int_list()
    print(f'List: {rand_list}')
    if binary_search(rand_list, user_input) is not None:
        print(f'Found {user_input} in index {rand_list}')
    else:
        print(f'Cannot find {user_input} in the list')
