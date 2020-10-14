"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dic_list = []                 # store dictionary into list


def main():
    print(f'Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ')
    read_dictionary()
    find_anagrams(input('Find anagrams for: '))


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                dic_list.append(word)


def find_anagrams(s):
    """
    :param s: user input
    :return:
    """
    ans_lst = []    # list of all anagrams answer
    ch_s = []       # the character of s
    i_lst = []      # the index of the character of s
    while s != EXIT:
        s = s.lower()
        find_anagrams_helper(s, ch_s, i_lst, ans_lst)
        print(f'{len(ans_lst)} anagrams: {ans_lst}')
        ans_lst.clear()
        s = input('Find anagrams for: ')


def find_anagrams_helper(s, ch_s, i_lst, ans_lst):
    """
    :param s: user input
    :param ch_s: the character of s
    :param i_lst: the index of the character of s
    :param ans_lst: list of all anagrams answer
    :return:
    """

    if len(ch_s) == len(s):
        ans = ""

        for i in range(len(ch_s)):
            ans += ch_s[i]

        print("Searching...")

        if has_prefix(ans, len(s), ans_lst):
            print(f'Found: {ans}')
            ans_lst.append(ans)
    else:
        for i in range(len(s)):
            if i not in i_lst:
                # Choose
                i_lst.append(i)
                ch_s.append(s[i])

                # Explore
                sub_s = ""
                for j in range(len(ch_s)):
                    sub_s += ch_s[j]

                if has_prefix(sub_s, len(s), ans_lst):
                    find_anagrams_helper(s, ch_s, i_lst, ans_lst)

                # Un-choose
                i_lst.pop()
                ch_s.pop()


def has_prefix(sub_s, s_len, ans_lst):
    """
    :param ans_lst:
    :param s_len: the length of s
    :param sub_s: substring of s
    :return: True or False, check whether sub_s is in dic_list
    """
    check = 0

    if len(sub_s) == s_len:
        if sub_s in dic_list and sub_s not in ans_lst:
            check = 1
    else:
        for word in dic_list:
            if word.startswith(sub_s):
                check = 1
                break

    if check == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
