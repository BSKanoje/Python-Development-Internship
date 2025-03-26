# Write a Python class to implement pow(x, n).

class PowerCalculator:
    def pow(self, x, n):
        if n == 0:
            return 1
        temp = self.pow(x, int(n / 2))
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp if n > 0 else (temp * temp) / x

calculator = PowerCalculator()
print(calculator.pow(2, 10))
print(calculator.pow(2, -2))
