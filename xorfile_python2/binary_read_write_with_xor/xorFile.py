from FileReadInLoop import FileReadInLoop

def xorFile(file1, file2, result ):
    oFileReadInLoop = FileReadInLoop(file1)
    
    # rb : readonly binary 
    fpRead = open(file2, "rb")

    # wb : writeonly binary
    fpWrite = open(result,'wb')

    byte = fpRead.read(1)
    while byte:
        fpWrite.write(   chr( 
                                ord(byte) ^ ord(oFileReadInLoop.nextByte()) 
                            ) 
                        )        
        byte = fpRead.read(1)
        
    fpRead.close()
    fpWrite.close()
    
