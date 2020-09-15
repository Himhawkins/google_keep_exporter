import gkeepapi

keep = gkeepapi.Keep()
print("Enter Username :")
a= raw_input()
print("Enter Password :")
b= raw_input()
keep.login(a,b)
#note = gkeepapi.createNote('Todo', 'Eat breakfast')

gnote = keep.get('1LaOnhCbJG7ezYFjaNRYl-FQrtaDUjBdC_Wr5uAmoxT74HX22T-9mh5OAvgovEKXD7PHi')
gnotes = keep.all()
text_file = open("KeepOutput.txt", "w")

for i in gnotes:
	n = text_file.write(i.title.encode('ascii', 'ignore'))
	print("Exporting note #")
	print(i.title.encode('ascii', 'ignore'))
	n = text_file.write('\n')
	n=  text_file.write(i.text.encode('ascii', 'ignore'))
        n = text_file.write('\n')
	n = text_file.write('___________________________________________________________')
	n = text_file.write('\n')
text_file.close()

print('All Done!!')
