from textwrap import wrap
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
def ascii_convert(ndx):
    key=list(range(32,127))
    key=key+list(range(192,256))

    value=[chr(i) for i in range(32, 127)]
    value=value+list([chr(i) for i in range(1040, 1104)])

    ascii_codes=dict(zip(key, value))
    if int(ndx) in ascii_codes:
        return ascii_codes[int(ndx)]
    else:
        return ''
    



alias=input("Введите исходную задачу: ")
start=alias[0]
alias=alias[1:]
alias=alias.replace(' ', '')
arr=[]

while len(alias)>0:
    counter=0
    i=0
    while alias[i]!='1':
        counter+=1
        i+=1
    arr.append(alias[0:counter*2+1])
    alias=alias[counter*2+1:len(alias)]

for i in range(len(arr)):
    arr[i]=convert_base(arr[i], 10, 2)

for i in range(len(arr)):
    arr[i]=start*int(arr[i])
    if start=='1':
        start='0'
    else:
        start='1'

s=''
for i in range(len(arr)):
    s+=str(arr[i])

s=wrap(s,8)
final=''
for i in range(len(s)):
    s[i]=convert_base(s[i], 10, 2)
    final+=ascii_convert(s[i])
print(final)