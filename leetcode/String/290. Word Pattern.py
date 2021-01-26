
'''

'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_dict = {}
        str_dict = {}
        str_word = str.split()
        if len(pattern) != len(str_word):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = i
            if str_word[i] not in str_dict:
                str_dict[str_word[i]] = i
        for i in range(len(pattern)):
            if pattern_dict[pattern[i]] != str_dict[str_word[i]]:
                return False
        return True
if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    print(solution.wordPattern(pattern,str))