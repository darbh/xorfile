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



