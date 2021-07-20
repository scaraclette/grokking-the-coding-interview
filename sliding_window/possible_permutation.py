"""
Permutation in a String (hard) #
Given a string and a pattern, 
find out if the string contains any permutation of the pattern.
"""

def find_permutation(str1, pattern):
    pattern_counter = {}

    for i in pattern:
        if i not in pattern_counter:
            pattern_counter[i] = 0
        pattern_counter[i] += 1

    window_start = 0
    matched = 0

    for window_end in range(len(str1)):
        char_end = str1[window_end]
        if char_end in pattern_counter:
            pattern_counter[char_end] -= 1
            if pattern_counter[char_end] == 0:
                matched += 1

        if matched == len(pattern):
            return True

        if window_end >= len(pattern) - 1:
            char_start = str1[window_start]
            window_start += 1
            if char_start in pattern_counter:
                if pattern_counter[char_start] == 0:
                    matched -= 1
                pattern_counter[char_start] += 1
        
    return False



def main():
#   print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
#   print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
#   print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()