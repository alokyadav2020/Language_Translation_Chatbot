from dataclasses import dataclass
from pathlib import Path



@dataclass()
class Model_Tokenizer:
    Model: None
    Tokenizer:None
 

@dataclass()
class DataTransfer:
 MESSAGE_TRANSFER = ""
 MESSAGE_RECIEVE =""
 AUDI_FILE: Path = None
 AUDI_FILE_S2C:Path =None
 DOC_FILE_S2C = None
 DOC_FILE_C2S = None
