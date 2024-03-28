def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def dynamic_programming_menu():
    print("Dynamic Programming Algorithms:")
    print("[1] Fibonacci Sequence")
    print("[2] Knapsack Problem")
    print("[3] Longest Common Subsequence")
    print("[4] Exit")

def perform_algorithm(choice):
    if choice == 1:
        n = int(input("Enter the value of n for Fibonacci sequence: "))
        print("Fibonacci sequence:")
        for i in range(n):
            print(fibonacci(i), end=" ")
    elif choice == 2:
        weights = list(map(int, input("Enter the weights: ").split()))
        values = list(map(int, input("Enter the values: ").split()))
        capacity = int(input("Enter the knapsack capacity: "))
        print("Maximum value:", knapsack(weights, values, capacity))
    elif choice == 3:
        s1 = input("Enter the first string: ")
        s2 = input("Enter the second string: ")
        print("Length of Longest Common Subsequence:", longest_common_subsequence(s1, s2))
    elif choice == 4:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")

while True:
    dynamic_programming_menu()
    choice = int(input("Enter your choice: "))
    perform_algorithm(choice)
