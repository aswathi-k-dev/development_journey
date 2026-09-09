class Factorial:
    def solution(self,num):
        factorial = 1
        for i in range(1,num+1):
            factorial = factorial*i
        print(factorial)

factorial_instance = Factorial()
factorial_instance.solution(6)