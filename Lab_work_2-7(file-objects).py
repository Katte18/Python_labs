#Lab. work 2-7 (file-objects)

#Write a script that creates a new output file called myfile.txt
inp = open('C:/Users/katia/Test1/lab2_7txt.', 'w')

#writes the string "Hello world file!" into it
inp.write('Hello world file!')
inp.close()

#write another code that opens myfile.txt in w+ mode
inp = open('C:/Users/katia/Test1/lab2_7txt.', 'r+')

#read and print its contents
print(inp.read())

#write into “Hello file” string new value “my” – “Hello my file”
inp.seek(len("Hello "))
inp.write("Hello my file ")

#Save changes without file object close
inp.flush()
inp.close()

output = open('C:/Users/katia/Test1/lab2_7txt.')
print(output.read())