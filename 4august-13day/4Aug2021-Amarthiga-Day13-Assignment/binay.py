file = open('test1.txt', 'w+b')
test =bytearray([12,34,56,34])
file.write(test)
file.close()
