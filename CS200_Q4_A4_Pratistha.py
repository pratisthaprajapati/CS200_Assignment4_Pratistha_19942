def is_composite(k):
    if k <= 0:
        return False

    n = k**2 + 2*k + 1
    for r in range(2, n):
        s = n // r
        if 1 < r < n and 1 < s < n:
            if r * s == n:
                return True
    return False

k = int(input("Enter the value of k (k > 0): "))


if is_composite(k):
    print(f"For k = {k}, k^2 + 2k + 1 is composite.")
else:
    print(f"For k = {k}, k^2 + 2k + 1 is prime.")