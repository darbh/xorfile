class FileReadInLoop:
	def __init__(self, filePathToRead):
		
		self.fpRead = open(filePathToRead, "rb+")
		
	def nextByte(self):
		byte=self.fpRead.read(1)
		if not byte:
			self.fpRead.seek(0)	
			byte=self.fpRead.read(1)		
		return byte

	def close(self):
		self.fpRead.close()


def xorfile(file1, file2, result ):
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
        
    oFileReadInLoop.close()
    fpRead.close()
    fpWrite.close()

def printHelp():
    print "\nInvalid Argumets\n\txorfile passwordFile inputFile outputFile\n\n"
    print """

# Encrypt File 
function xx(){
    local f=${1-""};
    local n=$(basename "${f}");
    local o="path-to-enc-dir/${n}";
    python path-to-xorfile.py path-to-password-file "${1}" "${o}"
}

# Decript File 
function xy(){
    local f=${1-""};
    local n=$(basename "${f}");
    local o="path-to-desc-dir/${n}";
    python path-to-xorfile.py path-to-password-file "${1}" "${o}"
}

    """
    
def main():
    import sys
    if 4 != len(sys.argv) :
        printHelp()
        return
        
    print "xorfile %s %s %s" % ( sys.argv[1] , sys.argv[2] , sys.argv[3]  )
    xorfile( sys.argv[1] , sys.argv[2] , sys.argv[3]  )
    
if __name__ == "__main__":
    main()
        
    
    
    
