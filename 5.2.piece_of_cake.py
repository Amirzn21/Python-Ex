def piece_of_cake(a, b):
    return a % b == 0 or b % a == 0

if __name__ == '__main__':
    print(piece_of_cake(10, 5))
