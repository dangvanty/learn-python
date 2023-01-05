text = input()
k= int(input())
output= ''
key = k%26
for i in text:
  if 65<=ord(i)<=90:
    buoc_nhay = ord(i) + key
    if ord(i) + key > 90: 
      buoc_nhay -= 26
      el = chr(buoc_nhay)
      output+=el
    else:
      el = chr(buoc_nhay)
      output+=el
  elif 97<=ord(i)<=122:
    buoc_nhay = ord(i) + key
    if buoc_nhay > 122: 
      buoc_nhay -= 26
      el = chr(buoc_nhay)
      output+=el
    else:
      el = chr(buoc_nhay)
      output+=el
  else:
    output+=i

print(output)