import sys


def main(N):
    if N == 1:
        fib_lst = [0]
    elif N == 2:
        fib_lst = [0, 1]
    else:
        fib_lst = [0, 1]
        for i in range(3, N + 1):
            pred, curr = 0, 1
            k = 2
            while k < i:
                pred, curr = curr, pred + curr
                k += 1
            fib_lst += [curr]
    print(fib_lst)


main(int(sys.argv[1]))
