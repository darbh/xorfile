# Enable Debuggung to see command executred 
set -x 
#removing result file if an y
rm -f out.gz 2>/dev/null 

# read in.gz and create out.gz 
python binary_read_write.py


zcat in.gz 


zcat out.gz
