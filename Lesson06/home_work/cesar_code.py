alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


put = int(input("message_cesar : " ))
message = input("message : " ).upper()
end = ''

for i in message:
 if i.upper() in alfavit:
    place = alfavit.find(i.upper())
    new_place = (place + put) % len(alfavit)
    new_char = alfavit[new_place]
    end += new_char if i.isupper() else new_char.lower()

 else:
     end += i
print(end)






