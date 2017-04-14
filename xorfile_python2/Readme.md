

# XOR files implemented in Python 2 

## Usage 
```
python xorfile/xorfile.py   passwordFilePath   inputFilepath   outputFilePath
```





## Some helper functions. Asumption. Fixed password and Destination for encrypt / decrypt  
```
function XOREncrypt(){
    local f=${1-""};
    local n=$(basename "${f}");
    local o="path-to-enc-dir/${n}";
    python path-to-xorfile.py path-to-password-file "${1}" "${o}"
}


function XORDecrypt(){
    local f=${1-""};
    local n=$(basename "${f}");
    local o="path-to-desc-dir/${n}";
    python path-to-xorfile.py path-to-password-file "${1}" "${o}"
}
```
