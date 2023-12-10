import string

lookup = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))


def solution(x):
    outp = ""
    for c in x:
        if c.islower():
            outp += lookup[c]
        else:
            outp += c
    return outp


def main():
    x = input('gib ')
    print(solution(x))       
    #print()


if __name__ == "__main__":
    main()
