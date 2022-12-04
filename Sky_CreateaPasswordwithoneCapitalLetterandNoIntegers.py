import re 

def Solution(text):
    l = 0
    list = re.split("[0-9]", text)
    for i in range(0,len(list)):
        if re.search("[A-Z]", list[i]):
            l1 = len(list[i])
            if l1 > l:
                l = l1
    return l

x = Solution('ab90ohjkhdfjaH02')
print(x)
