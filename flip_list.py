# Flip the Array
# Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.

# In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.

# Examples
# flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# # Take a horizontal list and flip it vertical.

# flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# # Take a vertical list and flip it horizontal.

# flip_list([]) ➞ []
# Notes
# If given an empty list [], return an empty list [].


def flip_list(lst):
    lst2 =[]
    for x in lst:
        if isinstance(x,int):
           lst2.append([int(digit) for digit in str(x)])
        elif isinstance(x,list):
             lst2.append(int(''.join(map(str, x))))
    return  lst2
print(flip_list([1, 2, 3, 4]))
print(flip_list([[5], [6], [9]]))





def flip_list(lst):
    lst2 = []
    
    for x in lst:
        if isinstance(x, int):
            # It's a horizontal list; we are flipping it to a vertical list
            lst2.append([x])
        elif isinstance(x, list):
            # It's a vertical list; we are flipping it to a horizontal list
            lst2.append(x[0])
    
    return lst2

# Test cases
print(flip_list([1, 2, 3, 4]))  # ➞ [[1], [2], [3], [4]]
print(flip_list([[5], [6], [9]]))  # ➞ [5, 6, 9]
print(flip_list([]))  # ➞ []







def flip_list(lst):
    if len(lst) == 0:
        return lst  # Return an empty list if input is empty
    if isinstance(lst[0], list):
        # It's a vertical list, so flatten it
        return [item[0] for item in lst]
    else:
        # It's a horizontal list, convert it to a vertical list
        return [[item] for item in lst]

# Test cases
print(flip_list([1, 2, 3, 4]))  # ➞ [[1], [2], [3], [4]]
print(flip_list([[5], [6], [9]]))  # ➞ [5, 6, 9]
print(flip_list([]))  # ➞ []
