# Enable Debuggung to see command executred 
set -x 
#removing result file if an y
rm -f in_2.gz 2>/dev/null
rm -f key_2   2>/dev/null

# read in.gz and create out.gz 
python test_xorFile.py


zcat in_2.gz 


cat key_2
