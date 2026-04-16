class Solution:
    def evalRPN(self, tokens):
        st = []
        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            else:
                b = st.pop()
                a = st.pop()
                
                if t == '+':
                    st.append(a + b)
                elif t == '-':
                    st.append(a - b)
                elif t == '*':
                    st.append(a * b)
                else:
                    st.append(int(a / b))
        return st[0]