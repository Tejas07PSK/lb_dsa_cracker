from collections import deque
class Solution:
    def ladderLength (self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited_word_states, wordList = set(), set(wordList)
        if (endWord not in wordList): return 0
        beginWord = list(beginWord)
        q = deque() ; q.append((beginWord, 1)) ; visited_word_states.add("".join(beginWord))
        while (q):
            curr_word, steps_travelled = q.popleft()
            for i in range(len(curr_word)):
                ori_chr = curr_word[i]
                for j in range(97, 123, 1):
                    curr_word[i] = chr(j)
                    next_possible_word = "".join(curr_word)
                    if ((next_possible_word in wordList) and (next_possible_word not in visited_word_states)):
                        if (next_possible_word == endWord): return steps_travelled + 1
                        visited_word_states.add(next_possible_word)
                        q.append((list(next_possible_word), (steps_travelled + 1)))
                curr_word[i] = ori_chr
        return 0
