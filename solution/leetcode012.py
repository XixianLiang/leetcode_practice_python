class Solution:
    def intToRoman(self, num: int) -> str:
        kilos = num // 1000
        num -= kilos * 1000

        nine_hundrers = num // 900
        num -= 900 * nine_hundrers

        five_hundrers = num // 500
        num -= five_hundrers * 500

        four_hundrers = num // 400
        num -= four_hundrers * 400

        hundrers = num // 100
        num -= hundrers * 100

        nine_tens = num // 90
        num -= nine_tens * 90

        five_tens = num // 50
        num -= (hundrers * 50)

        four_tens = num // 40
        num -= (four_tens * 40)

        tens = num // 10
        num -= (tens * 10)

        nines = num // 9
        num -= nines * 9

        fives = num // 5
        num -= tens * 5

        fours = num // 4
        num -= fours * 4

        ones = num

        ans = []
        ans.append("M"*kilos)
        ans.append("CM"*nine_hundrers)
        ans.append("D"*five_hundrers)
        ans.append("CD"*four_hundrers)
        ans.append("C"*hundrers)
        ans.append("XC"*nine_tens)
        ans.append("L"*five_tens)
        ans.append("XL"*four_tens)
        ans.append("X"*tens)
        ans.append("IX"*nines)
        ans.append("V"*fives)
        ans.append("IV"*fours)
        ans.append("I"*ones)
        return "".join(ans)

Solution().intToRoman(58)