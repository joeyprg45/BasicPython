text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
 
# TODO

new_test = text.replace(".","").replace(",","")
words = new_test.split() #splitって何？
print(words)    #この状態でリストになっている

lengh_list = list(map(len,words))
Ans = "".join(map(str, lengh_list))    
print(Ans)       #mapあり

A = ""
for i in words:
    A += str(len(i))
print(A)        #mapなし