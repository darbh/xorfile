from FileReadInLoop import FileReadInLoop

oFileReadInLoop = FileReadInLoop("key");

for i in range(100):
	ch = oFileReadInLoop.nextByte()
	print "%s %s" % ( i ,  ch  )




