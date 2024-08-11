import dpda_func as dpda

dpda = DPDA()
print(dpda.recognize("aabb"))   
print(dpda.recognize("abba"))   
print(dpda.recognize("bbaaa"))   
print(dpda.recognize("aabbaab")) 
