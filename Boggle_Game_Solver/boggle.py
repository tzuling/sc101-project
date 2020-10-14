"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dic_list = []


def main():
    """
    TODO:
    """
    read_dictionary()
    tmp = []
    user_input_matrix = []
    for i in range(4):
        user_input = input(f'{i+1} row of letters: ')
        if check_illegal(user_input):
            user_input = user_input.lower()
            for ch in user_input:
                if ch != " ":
                    tmp.append(ch)
            user_input_matrix.append(tmp)
            tmp = []
        else:
            break

    if len(user_input_matrix) == 4:
        find_boggle(user_input_matrix)


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                dic_list.append(word)


def find_boggle(user_input_matrix):
    """
    :param user_input_matrix: (2-D array) user input
    """
    ans = ''  # one of the boggle answer
    ans_lst = []  # list of all boggle answer

    for x in range(len(user_input_matrix)):
        for y in range(len(user_input_matrix[x])):
            find_boggle_helper(user_input_matrix, [(x, y)], ans, ans_lst)

    print(f'There are {len(ans_lst)} words in total.')


def find_boggle_helper(user_input_matrix, used_position, ans, ans_lst):
    """
    :param user_input_matrix: (2-D matrix) user input
    :param ans: (list) one of the boggle answer
    :param used_position:
    :param ans_lst: list of all boggle answer
    :return:
    """
    # Check word
    if len(ans) >= 4 and ans not in ans_lst:
        if ans in dic_list:
            print(f'Found \"{ans}\"')
            ans_lst.append(ans)

    # Recursion
    if has_prefix(ans):
        for i in range(-1, 2):
            for j in range(-1, 2):
                (x_curr, y_curr) = used_position[len(used_position) - 1]
                # Base Case
                if (x_curr + i, y_curr + j) not in used_position:
                    if 0 <= x_curr + i <= 3 and 0 <= y_curr + j <= 3:
                        # Choose
                        used_position.append((x_curr + i, y_curr + j))
                        ans += user_input_matrix[y_curr + j][x_curr + i]
                        # Explore
                        find_boggle_helper(user_input_matrix, used_position, ans, ans_lst)
                        # Un-choose
                        used_position.pop()
                        ans = ans[:len(ans)-1]


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic_list:
        if word.startswith(sub_s):
            return True
    return False


def check_illegal(s):
    """
    :param s: (String) user input
    :return: (Bool) check user input is illegal or not
    """
    check = 0
    for ch in s:
        if len(ch) > 1:
            check = 1

    if check == 0:
        return True
    else:
        print("Illegal input")
        return False


if __name__ == '__main__':
    main()
