from collections import deque
class Solution:
    def __words_differ_by_1 (self, word1, word2):
        j, count = 0, 0
        for i in range(len(word1)):
            if (word1[i] != word2[j]):
                count += 1
                if (count > 1): return False
            j += 1
        return True

    def ladderLength (self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList): return 0
        visited_word_states = set()
        q = deque() ; q.append((beginWord, 1)) ; visited_word_states.add(beginWord)
        while (q):
            curr_word, steps_travelled = q.popleft()
            for next_possible_word in wordList:
                if ((next_possible_word not in visited_word_states) and self.__words_differ_by_1(curr_word, next_possible_word)):
                    visited_word_states.add(next_possible_word)
                    q.append((next_possible_word, (steps_travelled + 1)))
                    if (next_possible_word == endWord): return steps_travelled + 1
        return 0
