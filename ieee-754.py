bits = input("Enter the base, default = 127") or 127
iee_binary = input("Enter the binary number").replace(" ","")
print(iee_binary)
sign = iee_binary[0]
number = iee_binary[1:8]
actual_number = iee_binary[9:]
number_size=8
number_holder=0
base_from = 2

for x in number:
    number_size-=1
    base_raised=int(base_from)**number_size
    number_multiplied=base_raised*int(x)
    number_holder=number_holder+number_multiplied

exp = number_holder
p = (exp - int(bits))

answer_in_binary = '1' + actual_number[0:p] + '.' + actual_number[p:] 
print(answer_in_binary)
