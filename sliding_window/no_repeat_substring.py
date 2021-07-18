def non_repeat_substring(s):
    if s == 0 or s == None:
        return 0
    start = 0
    end = 0
    sub_max = 0
    
    seen = set()
    
    while end < len(s):
        end_char = s[end]
        
        while end_char in seen:
            start_char = s[start]
            seen.remove(start_char)
            start += 1
            
        seen.add(end_char)
        sub_max = max(sub_max, end - start + 1)
        end += 1
            
    return sub_max

# Jump to next index without 2n solution
def alternative_non_repeat_substring(s):
    if s == 0 or s == None:
        return 0
    
    char_index = {}
    start = 0
    max_sub = 0

    for end in range(len(s)):
        end_char = s[end]
        if end_char in char_index:
            start = max(start, char_index[end_char] + 1)
        char_index[end_char] = end
        max_sub = max(max_sub, end - start + 1)
    
    return max_sub

if __name__=="__main__":
    print(non_repeat_substring("aabccbb"))
    print(non_repeat_substring("abbbb"))
    print(non_repeat_substring("abccde"))