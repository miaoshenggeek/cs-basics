class Solution:
    def calculate(self, s: str) -> int:
        # 3+2-3/4*5+3
        plus=s.split("+")
        res=0
        for num in plus:
            if num.strip(" ").isdigit():
                res+=int(num.strip(" "))
            else:
                
                sub=num.split("-")
                for i,s in enumerate(sub):
                    if s.strip(" ").isdigit():
                        if i==0: res+=int(s.strip(" "))
                        else:res-=int(s.strip(" "))
                    else:
                        mul=s.split("*")
                        ans=1
                        for j,m in enumerate(mul):
                            if m.strip(" ").isdigit():
                                ans=ans*int(m.strip(" "))
                            else:
                                de=m.split("/")
                                for k,d in enumerate(de):
                                    if d.strip(" ").isdigit():
                                        if k==0:ans=ans*int(d.strip(" "))
                                        else:ans=ans//int(d.strip(" "))
                        if i==0:res+=ans
                        else:res-=ans
        return res

        
    def calculate_stack(s):
        cur, stack, op = 0, [], '+'
        for c in s + '+':
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(cur)
                elif op == '-':
                    stack.append(-cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                else:
                    stack.append(int(stack.pop() / cur))
                cur = 0
                op = c
        return sum(stack)