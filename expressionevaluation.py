平时我们对于四则运算的表达式是比如：“（3+3）*4-（8/4）”这个样子的。我们可以清楚的分辨出括号和运算符的优先级，然后进行计算。可是如何用程序来实现这一功能呢？

我们需要借助另一种不需要括号的后缀表示法，也称为逆波兰表示法（Reverse Polish Notation，RPN）。

比如说“（3+3）*4-（8/4）”这个表达式，转换成后缀表示，就是“3 3 + 4 * 8 4 /-”，对于这种表达式，
计算机程序很容易处理，只要按照这个规则：
从左到右遍历表达式，遇到数字就进栈，遇到运算符就从栈中弹出两个数值进行计算，将计算结果再进栈。最后栈中只剩下一个元素的时候就是计算结果了。

那么，这个问题剩下的难点就是，如何将中缀表达式，用计算机转换成后缀表达式。或者更通俗点说，就是如何不用括号，将中缀表达式的优先级还有计算顺序表达出来。

这里，我们还要用到栈，从左到右遍历中缀表达式，如果是数字直接输出，如果是符号：
1、如果是左括号‘（’直接进栈。
2、如果是‘）’右括号，将符号按顺序出栈直到遇到第一个左括号为止。
3、若是+ - * /四个运算符，则与栈顶的运算符相比较，如果优先级高，直接进栈，如果优先级要低于栈顶优先级，那将栈顶元素出栈输出，然后继续比较，直到该运算符进栈或者栈空为止。
如此做，最后输出的就是这个中缀表达式的后缀形式了。

我自己写了一个，将这两步写在了一起，使用了两个栈，一个是数字栈，一个是符号栈，边判断着符号的优先级边计算，其实原理是一样的。不过当栈中的符号输出的时候，我是直接从数据栈里弹出两个元素计算之后进栈。

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        tokens = self.toRPN(s)
        return self.evalRPN(tokens)

    operators = ['+', '-', '*', '/']

    def toRPN(self, s):
        tokens, stack = [], []
        number = ''
        for c in s:
            if c.isdigit():
                number += c
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if c in self.operators:
                    while len(stack) and self.getPriority(stack[-1]) >= self.getPriority(c):
                        tokens.append(stack.pop())
                    stack.append(c)
                elif c == '(':
                    stack.append(c)
                elif c == ')':
                    while len(stack) and stack[-1] != '(':
                        tokens.append(stack.pop())
                    stack.pop()
        if number:
            tokens.append(number)
        while len(stack):
            tokens.append(stack.pop())
        return tokens

    def evalRPN(self, tokens):
        operands = []
        for token in tokens:
            if token in self.operators:
                y, x = operands.pop(), operands.pop()
                operands.append(self.getVal(x, y, token))
            else:
                operands.append(int(token))
        return operands[0]
    
    def getVal(self, x, y, operator):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y),
        }[operator](x, y)

    def getPriority(self, operator):
        return {
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
        }.get(operator, 0)