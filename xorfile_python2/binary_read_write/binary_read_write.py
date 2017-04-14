
# rb : readonly binary 
fpRead = open("in.gz", "rb")

# wb : writeonly binary
fpWrite = open('out.gz','wb')

byte = fpRead.read(1)
while byte:
    fpWrite.write(byte)        
    byte = fpRead.read(1)
    
fpRead.close()
fpWrite.close()

