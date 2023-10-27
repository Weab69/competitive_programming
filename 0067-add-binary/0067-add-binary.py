class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = 0
        int_b = 0
        for i in range(len(a)):
            int_a +=int(a[i])*2**(len(a)-1-i)
        for i in range(len(b)):
            int_b += int(b[i])*2**(len(b)-1-i)
        
        n = int_a+int_b
        result = ''
        if n !=0:
            while True:
                if n != 0:
                    v = n%2
                    result = str(v)+result
                else:
                    break
                n = n//2
            return result
        return '0'