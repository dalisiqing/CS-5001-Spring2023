def add_list(ls):
    """Add up a list of numbers recursively"""
    if not len(ls):
        return 0
    else:
        return ls[0] + add_list(ls[1:])

print("Add list non-tail recursive")
print(add_list([1, 2, 3, 4, 5]))


def add_list_tr(ls, ind, total):
    """Add up a list of values recursively using tail recursion"""
    if ind == len(ls):
        return total
    else:
        return add_list_tr(ls, ind+1, total+ls[ind])

print("Add list tail recursive")
print(add_list_tr([1, 2, 3, 4, 5], 0, 0))


def rev_list(ls):
    """Reverse a list recursively"""
    if len(ls) == 0:
        return []
    else:
        return [ls[-1]] + rev_list(ls[:-1])

print("Reverse list rev_list")
print(rev_list([1, 2, 3, 4, 5]))


def rev_list_tr(input, output, length):
    """Reverse a list using tail recursion"""
    if not length:
        return output
    else:
        return rev_list_tr(input[:-1], output + input[-1:], length - 1)

print("Reverse list rev_list_tr")
print(rev_list_tr([1, 2, 3, 4, 5], [], 5))


def linear_search(val, ls):
    """Find index of val recursively"""
    if not ls:  # base case: empty list
        return -1
    elif ls[0] == val:  # base case: found value
        print("Comparing:", ls[0], "and", val, "are equal")
        return 0
    else:
        print("Comparing:", ls[0], "and", val, "are not equal")
        index = linear_search(val, ls[1:])  # recursive call
        if index == -1:
            return -1
        else:
            return index + 1

print("Linear search:")
print(linear_search(1, [1, 2, 3, 4, 5]))
print(linear_search(4, [1, 2, 3, 4, 5]))
print(linear_search(6, [1, 2, 3, 4, 5]))


def linear_search_tr(val, ls, ind):
    """Find index of val using tail recursion"""
    if ind == len(ls):
        return -1
    elif ls[ind] == val:
        print("Comparing:", ls[ind], "and", val, "are equal")
        return ind
    else:
        print("Comparing:", ls[ind], "and", val, "are not equal")
        return linear_search_tr(val, ls, ind + 1)

print("Linear search tail recursive:")
print(linear_search_tr(1, [1, 2, 3, 4, 5], 0))
print(linear_search_tr(4, [1, 2, 3, 4, 5], 0))
print(linear_search_tr(6, [1, 2, 3, 4, 5], 0))


def binary_search_tr(x, lower, ls):
    """Recursive binary search
    using tail recursion"""
    mid = int(len(ls)/2)
    if ls == []:
        return -1
    if x == ls[mid]:
        print("Comparing:", ls[mid], "and", x, "are equal")
        return lower + mid
    elif x > ls[mid]:
        lower = mid + 1
        print("Comparing:", x, "is greater than", ls[mid])
        return binary_search_tr(x, lower, ls[lower:])
    else:
        print("Comparing:", x, "is less than", ls[mid])
        return binary_search_tr(x, lower, ls[:mid])

print("Binary search tail recursion:")
print(binary_search_tr(1, 0, [1, 2, 3, 4, 5]))
print(binary_search_tr(4, 0, [1, 2, 3, 4, 5]))
print(binary_search_tr(6, 0, [1, 2, 3, 4, 5]))


def binary_search(x, ls):
    """Recursive binary search
    using non-tail recursion"""
    mid = int(len(ls)/2)
    if len(ls) == 0:
        return -1
    if x == ls[mid]:
        print("Comparing:", ls[mid], "and", x, "are equal")
        return mid
    elif x > ls[mid]:
        print("Comparing:", x, "is greater than", ls[mid])
        if binary_search(x, ls[mid+1:]) == -1:
            return -1
        else:
            return mid + 1 + binary_search(x, ls[mid+1:])
    else:
        print("Comparing:", x, "is less than", ls[mid])
        return binary_search(x, ls[:mid])

print("Binary search non-tail recursion:")
print(binary_search(1, [1, 2, 3, 4, 5]))
print(binary_search(4, [1, 2, 3, 4, 5]))
print(binary_search(6, [1, 2, 3, 4, 5]))


def bubble_sort(ls):
    """Recursive bubble sort"""
    if len(ls) <= 1:
        return ls
    if len(ls) == 2:
        if ls[0] < ls[1]:
            return ls
        else:
            return [ls[1], ls[0]]

    a, b, c = ls[0], ls[1], ls[2:]
    store = []
    if a < b:
        store = [a] + bubble_sort([b] + c)
    else:
        store = [b] + bubble_sort([a] + c)
    return bubble_sort(store[:-1]) + store[-1:]

print("Bubble sort")
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 1, 2]))





    

