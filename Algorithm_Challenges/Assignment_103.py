#103.Longest Common Substring Find the longest common substring between two given strings.
def find_longest_common_substring(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_length, end_index = 0, 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length, end_index = max((max_length, end_index), (dp[i][j], i))

    return s1[end_index - max_length:end_index]

s1, s2 = "abcde", "bcdef"
print("Longest Common Substring:", find_longest_common_substring(s1, s2))
