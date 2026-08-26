# Brute force approach

# s = "anagram"
# t = "nagaramm"

# fre_s = {}
# fre_t = {}

# def frequency(word, freq) :
#     for i in word :
#         if i not in freq :
#             freq[i] = 1
#         else :
#             freq[i] += 1

# frequency(s,fre_s)
# frequency(t,fre_t)

# if fre_s != fre_t :
#     print("Not anagram")
# else :
#     print("Yes Angaram")


# Better Solution

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print("Not Anagram")
else:
    freq = {}

    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1
        freq[t[i]] = freq.get(t[i], 0) - 1

    is_anagram = True

    for value in freq.values():
        if value != 0:
            is_anagram = False
            break

    print("Yes Anagram" if is_anagram else "Not Anagram")



    






    