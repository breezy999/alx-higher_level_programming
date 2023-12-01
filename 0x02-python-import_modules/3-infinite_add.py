#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            n = n + int(arg)
    print(n)
