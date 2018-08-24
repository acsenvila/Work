str = input ("enter anything")
digit = 0
letters = 0
for i in str:
 if i.isalpha():
  letters += 1
 elif i.isdigit():
  digit += 1
print (letters, digit)
