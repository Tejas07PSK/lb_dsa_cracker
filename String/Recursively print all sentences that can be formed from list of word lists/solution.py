class Solution:
    def printSentences (self, list_of_word_lists, size, current_itr, str_list):
        if (current_itr == size):
            print(" ".join(str_list))
            return
        for string in list_of_word_lists[current_itr]:
            str_list[current_itr] = string
            self.printSentences(list_of_word_lists, size, (current_itr + 1), str_list)
