class FizzBuzzStudy():

    def __init__(self):
        pass

    def is_fizz_or_buzz(self, number):

        if self.is_fizz(number) and self.is_buzz(number):
            return "fizzbuzz"
        elif self.is_fizz(number):
            return "fizz"
        elif self.is_buzz(number):
            return "buzz"
        else:
            return number

    def is_fizz(self, number):
        return number % 3 == 0

    def is_buzz(self, number):
        return number % 5 == 0

    def _100_fizz_buzz_calls(self):
        for num in range(101):
            print(self.is_fizz_or_buzz(num))



if __name__ == "__main__":
    fizzbuzz = FizzBuzzStudy()
    for num in range(101):
        print(fizzbuzz.is_fizz_or_buzz(num))





