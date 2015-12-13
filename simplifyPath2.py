class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path = path.split('/')
        curr = '/'
        for i in path:
            if i == '..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '': curr = '/'
            elif i != '.' and i != '':
                curr += '/' + i if curr != '/' else i
        return curr