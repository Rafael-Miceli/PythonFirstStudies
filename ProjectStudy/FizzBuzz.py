class FizzBuzzStudy():

    def is_fizz_or_buzz(self, number):
        if number % 3 == 0:
            return "fizz"
        elif number % 5 == 0:
            return "buzz"
        else:
            return number


