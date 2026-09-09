class Gcd:
    def solution(self,num1,num2):
        gcd = 1
        for i in range(2,min(num1,num2)+1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i
        print(gcd)

gcd_instance = Gcd()
gcd_instance.solution(12,18)