myfile=open("demo.bin",'w+b')
text=bytearray([12,23,45])
myfile.write(text)
myfile.close()

