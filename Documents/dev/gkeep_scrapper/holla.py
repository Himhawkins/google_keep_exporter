import gkeepapi

keep = gkeepapi.Keep()
keep.login('example@example.com', 'password')
gnotes = keep.all()

#print (gnotes)
#print (note.text)
for i in gnotes:
    if i.title!='':
        print(i.title)