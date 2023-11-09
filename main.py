def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    # initializes counts list
    counts[n] += 1
    ###TODO
    # base case: checks if the term number is 0 or 1 (their corresponding fibonacci terms match the term number)
    if n == 0 or n == 1:
        return n
    # recursive case: gets previous two terms and adds them together by calling the function recursively
    else:
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)

    
def fib_top_down(n, fibs):
    ###TODO
    # checks if the value has been computed yet
    if fibs[n] == -1:
        # base case (similar to original recursive implementation)
        if n == 0 or n == 1:
            # updates list of computed values with the new calculated value
            fibs[n] = n
            # returns updated list of computed values
            return fibs[n]
        # recursive case: similar to original recursive implementation, except stores it in list of computed values
        else:
            fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
    # if value has already been computed, simply return value in given list index
    else:
        return fibs[n]


def fib_bottom_up(n):
    ###TODO
    pass