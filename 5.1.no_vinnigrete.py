def no_vinnigrete(lst):
    return [item for item in lst if item]

if __name__ == '__main__':
    print(no_vinnigrete([None, 1, 0, '', 'Hello']))
