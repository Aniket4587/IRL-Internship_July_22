import re
S=input()
m=re.search(r'((\w(?!_))\2{1,})',S)
print(S[m.start()] if m else '-1')
