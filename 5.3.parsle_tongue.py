def parsle_tongue(s: str) -> str:
    return s.replace('s', 'sss').replace('S', 'SSS')

if __name__ == '__main__':
    print(parsle_tongue("silly snakes"))
