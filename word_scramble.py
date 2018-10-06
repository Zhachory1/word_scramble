import sys
import collections
import copy


def find_words(needed_char, opt_chars):
  chars = collections.Counter(needed_char + opt_chars)
  words = []
  count = 0
  with open('/usr/share/dict/english3.txt') as inf:
    for line in inf:
      line = line.lower().strip()
      count += 1
      if count % 1000 == 0:
        print("At count", count, "and found", len(words)) 
      if needed_char in line:
        temp = copy.deepcopy(chars)
        current_word = collections.Counter(line)
        temp.subtract(current_word)
        possible_word = True
        for val in temp.values():
          if val < 0:
            possible_word = False
            break
        if possible_word:
          words.append(line)
  return words


def word_scramble_main(needed_char, opt_chars):
  words = find_words(needed_char, opt_chars)
  count = 0
  print()
  for word in words:
    if len(word) == 8:
      print(word, end=" ")
      count += 1
      if count % 10 == 9:
        print()
  print("\nNumber of words:", count)

def main():
  needed_char, opt_chars = sys.argv[1], sys.argv[2]
  word_scramble_main(needed_char, opt_chars)


if __name__ == '__main__':
    main()