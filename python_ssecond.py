digits_given = 234
numbers_vs_characters = { "2":'abc',  "3":'def',\
                     "4":'ghi',  "5":'jkl',\
                     "6":'mno',  "7":'pqrs',\
                     "8":'tuv',  "9":'wxyz'}
output = [""]
for d in str(digits_given):
    output = [i+j for i in output for j in numbers_vs_characters[d]]
    print(output)
if output == [""]:
    output = [] 