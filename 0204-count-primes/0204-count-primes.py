class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        
        is_prime = [False, False] + [True] * (n - 2)
        
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
               
                m = i
                while i * m < n:
                    is_prime[i * m] = False
                    m += 1

        return sum(is_prime)