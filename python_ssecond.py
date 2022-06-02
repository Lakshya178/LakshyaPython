digits = 234
dispatch = { "2":'abc',  "3":'def',\
                     "4":'ghi',  "5":'jkl',\
                     "6":'mno',  "7":'pqrs',\
                     "8":'tuv',  "9":'wxyz'}
output = [""]
for d in str(digits):
    output = [i+j for i in output for j in dispatch[d]]
    print(output)
if output == [""]:
    output = [] 