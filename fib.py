# memorization : store duplicate subproblems

def fib(n, memo=None):
    """
        Return nth fibonnaci number
        Parameters:
            n (int) : Unsigned Integer
            memo (dict): Dictionary that holds returned value of f(n) with key n
    """
    if memo is None: memo={}
    if (n in memo): return memo[n]
    if (n<=2): return 1
    memo[n] = fib(n-1, memo)+fib(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    print(fib(50))   #12586269025
