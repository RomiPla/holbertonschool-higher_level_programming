#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for liste in dir(hidden_4):
        if (liste[0] != '_' and liste[1] != '_'):
            print(liste)
