def thats_the_way(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split('_'))

if __name__ == '__main__':
    print(thats_the_way("hello_world"))
