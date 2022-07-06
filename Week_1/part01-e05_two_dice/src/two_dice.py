#!/usr/bin/env python3

def main():
    for i in range (1,7):
        for s in range (1,7):
            if (i+s == 5):
                print((i,s))

if __name__ == "__main__":
    main()
