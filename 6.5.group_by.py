from collections import Counter

def group_by(lst):
    return dict(Counter(lst))

if __name__ == '__main__':
    print(group_by([1, 2, 2, 3, 3, 3]))
