class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        tail = 0
        for i in range(len(chars)):
            if ord(chars[i])>= ord("a") and ord(chars[i])<= ord("z"):
                chars[i], chars[tail] = chars[tail], chars[i]
                tail += 1
            