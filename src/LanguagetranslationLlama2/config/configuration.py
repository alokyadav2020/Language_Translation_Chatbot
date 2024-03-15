from src.LanguagetranslationLlama2.constants import *
from src.LanguagetranslationLlama2.entity import Model_Tokenizer


class ConfigurationManager:
    def __init__(self) -> None:
        pass




    def get_model_tokenizer(self)-> Model_Tokenizer:

        model_tokenizer_config = Model_Tokenizer(

            Model=MODEL,
            Tokenizer=TOKENIZER

        )
        return model_tokenizer_config