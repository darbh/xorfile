
from FileReadInLoop import FileReadInLoop
from xorFile import xorFile



xorFile("key","in.gz", "encipted")
xorFile("key","encipted", "in_2.gz")
xorFile("in.gz","encipted", "key_2")




