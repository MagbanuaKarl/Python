def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def miscellaneous_algorithms_menu():
    print("Miscellaneous Algorithms:")
    print("[1] Sieve of Eratosthenes (Prime Number Generation)")
    print("[2] Euclidean Algorithm (Greatest Common Divisor)")
    print("[3] Exit")

def perform_algorithm(choice):
    if choice == 1:
        n = int(input("Enter the value of n for Sieve of Eratosthenes: "))
        print("Prime numbers up to", n, ":", sieve_of_eratosthenes(n))
    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Greatest Common Divisor:", euclidean_algorithm(a, b))
    elif choice == 3:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")

while True:
    miscellaneous_algorithms_menu()
    choice = int(input("Enter your choice: "))
    perform_algorithm(choice)
