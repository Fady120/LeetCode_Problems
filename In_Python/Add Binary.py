class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result = []

        carry_ya_alby = 0

        lenght_a = len(a) - 1
        lenght_b = len(b) - 1

        while lenght_a >= 0 or lenght_b >= 0 or carry_ya_alby:
            if lenght_a >= 0:
                carry_ya_alby += int(a[lenght_a])
                lenght_a -= 1
            if lenght_b >= 0:
                carry_ya_alby += int(b[lenght_b])
                lenght_b -= 1
            result.append(str(carry_ya_alby % 2))
            carry_ya_alby //= 2
        
        return ''.join(reversed(result))
