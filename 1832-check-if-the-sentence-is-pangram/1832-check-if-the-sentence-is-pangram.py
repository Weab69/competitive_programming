class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return 26==len(set(sentence))
        