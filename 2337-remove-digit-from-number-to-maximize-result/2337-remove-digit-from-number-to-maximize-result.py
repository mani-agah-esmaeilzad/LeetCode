class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max = "0"

        for i in range(len(number)):
            print(i)
            if number[i] == digit:
                temp = number[:i] + number[i+1:]
                print(temp)
                print(number[i])
                if temp > max:
                    max = temp

        return max