class Leap_Year:
    def solution(self,year):
        if (year % 100 ==0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            print("leap year")
        else:
            print("not a leap year")

leap_year_instance = Leap_Year()
leap_year_instance.solution(2026)
leap_year_instance.solution(2024)