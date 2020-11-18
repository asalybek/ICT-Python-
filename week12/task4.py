# 128
# dictionary = {
#     "001": "Mobile",
#     "002": "Desktop",
#     "003": "Laptop",
#     "004": "Laptop"
# }
#
#
# def reverse_lookup(dict, value):
#     keys = []
#     for i in dict:
#         if value == dict[i]:
#             keys.append(i)
#     print(keys)
#
#
# def main():
#     reverse_lookup(dictionary, "Mobile")
#     reverse_lookup(dictionary, "Laptop")
#     reverse_lookup(dictionary, "Smartwatch")
#
#
# if __name__ == '__main__':
#     main()

# 129
# from random import randint
#
#
# def two_dice_roll_add():
#     dice1 = randint(1, 6)
#     dice2 = randint(1, 6)
#     return dice1 + dice2
#
#
# def main():
#     result_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
#
#     for turn in range(1000):
#         result = two_dice_roll_add()
#         result_dict[result] += 1
#
#     print("Total".rjust(16), "|", "Simulated %".rjust(16), "|", "Expected %".rjust(16))
#     print("-------------------------------------------------------")
#     for n in range(2, 13):
#         sim_result = str("%.2f" % (result_dict[n] / 1000 * 100))
#         if n <= 7:
#             exp_result = str("%.2f" % ((n - 1) / 36 * 100))
#         else:
#             exp_result = str("%.2f" % ((12 - n + 1) / 36 * 100))
#         print(str(n).rjust(16), "|", sim_result.rjust(16), "|", exp_result.rjust(16))
#
#
# if __name__ == '__main__':
#     main()

# 130
# dictionary = {
#     ".": "1", ",": "11", "?": "111", "!": "1111", ":": "11111",
#     "A": "2", "B": "22", "C": "222",
#     "D": "3", "E": "33", "F": "333",
#     "G": "4", "H": "44", "I": "444",
#     "J": "5", "K": "55", "L": "555",
#     "M": "6", "N": "66", "O": "666",
#     "P": "7", "Q": "77", "R": "777", "S": "7777",
#     "T": "8", "U": "88", "V": "888",
#     "W": "9", "X": "99", "Y": "999", "Z": "9999",
#     " ": "0"
# }
#
#
# def reverse_lookup(s):
#     keys = ""
#     for i in s:
#         keys += dictionary[i]
#     print(keys)
#
#
# reverse_lookup("Hello, World!".upper())

# 131
# alph_morse = {'A': '.-', 'B': '-...',
#               'C': '-.-.', 'D': '-..', 'E': '.',
#               'F': '..-.', 'G': '--.', 'H': '....',
#               'I': '..', 'J': '.---', 'K': '-.-',
#               'L': '.-..', 'M': '--', 'N': '-.',
#               'O': '---', 'P': '.--.', 'Q': '--.-',
#               'R': '.-.', 'S': '...', 'T': '-',
#               'U': '..-', 'V': '...-', 'W': '.--',
#               'X': '-..-', 'Y': '-.--', 'Z': '--..',
#               '1': '.----', '2': '..---', '3': '...--',
#               '4': '....-', '5': '.....', '6': '-....',
#               '7': '--...', '8': '---..', '9': '----.',
#               '0': '-----'}
#
#
# def encrypt_msg(charr):
#     return alph_morse[charr] + " "
#
#
# s = input()
# res = ""
# for ch in s:
#     if ch.isdigit() or ch.isalpha():
#         res += encrypt_msg(ch.upper())
#     else:
#         continue
# print(res)

# 132
# province_code = {
#     "A": "Newfoundland", "B": "Nova Scotia", "C": "Prince Edward Island",
#     "E": "New Brunswick", "G": "Quebec", "H": "Quebec", "J": "Quebec",
#     "K": "Ontario", "L": "Ontario", "M": "Ontario", "N": "Ontario",
#     "P": "Ontario", "R": "Manitoba", "S": "Saskatchewan", "T": "Alberta",
#     "V": "British Columbia", "X": ["Nunavut", "Northwest Territories"], "Y": "Yukon"}
#
#
# def reverse_lookup(s):
#     keys = ""
#     if len(province_code[s[0]]) == 1:
#         keys += str(province_code[s[0]])
#     else:
#         for s in province_code[s[0]]:
#             keys += s + ", "
#     if s[1] == 0:
#         keys += " rural"
#     else:
#         keys += " urban"
#     print(keys)
#
#
# s = input()
# if s[0] in province_code.keys():
#     reverse_lookup(s)
# else:
#     print("Invalid postal code")

# 133
# dictionary = {
#     1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
#     9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
#     16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
#     50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 0: 'zero'
# }
#
#
# def convert_to_words(n):
#     if n > 99:
#         print(dictionary[int(n / 100)] + ' hundred ', end='')
#         n = n - int(n / 100) * 100
#     if n in dictionary.keys():
#         print(dictionary[n])
#     else:
#         print(dictionary[n - n % 10] + ' ' + dictionary[n % 10])
#
#
# number = int(input())
# convert_to_words(number)


# 134
# def reverse_lookup(s):
#     print(len(set(s)))
#
#
# s = input()
# reverse_lookup(s)

# 135
# def count_letter_frequency(word):
#     letter_frequency = {}
#     for letter in word:
#         keys = letter_frequency.keys()
#         if letter in keys:
#             letter_frequency[letter] += 1
#         else:
#             letter_frequency[letter] = 1
#     return letter_frequency
#
# s1 = input()
# s2 = input()
# if count_letter_frequency(s1) == count_letter_frequency(s2):
#     print("Anagram")
# else:
#     print("No Anagram")

# 136
# def count_letter_frequency(word):
#     letter_frequency = {}
#     for letter in word:
#         keys = letter_frequency.keys()
#         if letter.isalpha():
#             if letter in keys:
#                 letter_frequency[letter] += 1
#             else:
#                 letter_frequency[letter] = 1
#     return letter_frequency
#
#
# s1 = input()
# s2 = input()
# if count_letter_frequency(s1.lower()) == count_letter_frequency(s2.lower()):
#     print("Anagram")
# else:
#     print("No Anagram")

# 137
# scrabble_scores = {"A": 1, "B": 3, "C": 3, "D": 2,
#                    "E": 1, "F": 4, "G": 2, "H": 4,
#                    "I": 1, "J": 8, "K": 5, "L": 1,
#                    "M": 3, "N": 1, "O": 1, "P": 3,
#                    "Q": 10, "R": 1, "S": 1, "T": 1,
#                    "U": 1, "V": 4, "W": 4, "X": 8,
#                    "Y": 4, "Z": 10}
#
#
# def get_score(word):
#     total_score = 0
#     for ch in word:
#         total_score += scrabble_scores[ch]
#     return total_score
#
#
# s = input()
# print(str(get_score(s.upper())))

# 138
# import random
#
#
# def get_bingo_card():
#     gridSize = 5
#
#     bingo_card = {}
#     randRange = range(1, 15)
#     values = random.sample(randRange, gridSize)
#     bingo_card['B'] = values
#
#     values = []
#     randRange = range(16, 30)
#     values = random.sample(randRange, gridSize)
#     bingo_card['I'] = values
#
#     values = []
#     randRange = range(31, 45)
#     values = random.sample(randRange, gridSize)
#     bingo_card['N'] = values
#
#     values = []
#     randRange = range(46, 60)
#     values = random.sample(randRange, gridSize)
#     bingo_card['G'] = values
#
#     values = []
#     randRange = range(61, 75)
#     values = random.sample(randRange, gridSize)
#     bingo_card['O'] = values
#
#     return bingo_card
#
#
# def print_bingo_card(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))
#
#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))
#
#
# print_bingo_card(get_bingo_card())

# 139
# def check_bingo(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     # check vertical line
#     for h in head:
#         sum = 0
#         for i in card[h]:
#             sum = sum + i
#         if sum == 0:
#             return True
#
#     # check horizontal line
#     for i in range(0, 5):
#         sum = 0
#         for h in head:
#             sum = sum + card[h][i]
#         if sum == 0:
#             return True
#
#     # check diagonal line
#     sum = card['B'][0] + card['I'][1] + card['N'][2] + card['G'][3] + card['O'][4]
#     if sum == 0:
#         return True
#     # check another diagonal line
#     sum = card['B'][4] + card['I'][3] + card['N'][2] + card['G'][1] + card['O'][0]
#     if sum == 0:
#         return True
#
#     return False
#
#
# def print_bingo(card):
#
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))
#
#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))
#     print("\n")
#
#
# def main():
#     card = {'B': [7, 15, 11, 2, 10],
#             'I': [25, 22, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 55, 59],
#             'O': [62, 70, 74, 68, 75]}
#
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [0, 0, 0, 0, 0],
#             'I': [25, 22, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 55, 59],
#             'O': [62, 70, 74, 68, 75]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [7, 0, 11, 2, 10],
#             'I': [25, 0, 30, 28, 27],
#             'N': [44, 0, 0, 37, 39],
#             'G': [57, 0, 46, 55, 59],
#             'O': [62, 0, 74, 68, 75]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [0, 15, 11, 2, 10],
#             'I': [25, 0, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 0, 59],
#             'O': [62, 70, 74, 68, 0]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#
# if __name__ == "__main__":
#     main()

# 140
# import random
#
#
# def get_bingo_card():
#     gridSize = 5
#
#     bingo_card = {}
#     randRange = range(1, 15)
#     values = random.sample(randRange, gridSize)
#     bingo_card['B'] = values
#
#     values = []
#     randRange = range(16, 30)
#     values = random.sample(randRange, gridSize)
#     bingo_card['I'] = values
#
#     values = []
#     randRange = range(31, 45)
#     values = random.sample(randRange, gridSize)
#     bingo_card['N'] = values
#
#     values = []
#     randRange = range(46, 60)
#     values = random.sample(randRange, gridSize)
#     bingo_card['G'] = values
#
#     values = []
#     randRange = range(61, 75)
#     values = random.sample(randRange, gridSize)
#     bingo_card['O'] = values
#
#     return bingo_card
#
#
# def check_for_bingo_value(val):
#     cur_bingo_card = get_bingo_card()
#     for i in cur_bingo_card:
#         if int(val[1:]) in cur_bingo_card[i]:
#             print( cur_bingo_card[i][int(val[1:])])
#             cur_bingo_card[i][int(val[1:])] = 0
#
#     print_bingo_card(cur_bingo_card)
#
#
# def print_bingo_card(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))
#
#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))
#
#
# check_for_bingo_value("B12")