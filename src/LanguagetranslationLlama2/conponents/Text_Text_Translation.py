from transformers import SeamlessM4TForTextToText,SeamlessM4TForSpeechToText,SeamlessM4TForTextToSpeech,SeamlessM4TForSpeechToSpeech,AutoProcessor

from src.LanguagetranslationLlama2.constants import DIRECTORY,FILENAME
import os


class Text_Translation:
    def __init__(self): #Model_Tokenizer_config: Model_Tokenizer
        # self.M_T_Config = Model_Tokenizer_config

        model_path = os.path.join(DIRECTORY, FILENAME)

        # self.M_T_Config.Tokenizer = AutoProcessor.from_pretrained(model_path)
        # self.M_T_Config.Model = SeamlessM4TForTextToText.from_pretrained(model_path)

        # Processor like tokenizer  
        self.Processor = AutoProcessor.from_pretrained(model_path)
        #Text to Text translation model
        self.T2TT_Model = SeamlessM4TForTextToText.from_pretrained(model_path)
        #Text to speech translation model
        # self.T2ST_Model = SeamlessM4TForTextToSpeech.from_pretrained(model_path)
        # #Speech to Text translation model
        # self.S2TT_Model = SeamlessM4TForSpeechToText.from_pretrained(model_path)
        # #Speech to Speech translation model
        # self.S2ST_Model = SeamlessM4TForSpeechToSpeech.from_pretrained(model_path)


    def Text_2_Text_Translate(self,text_input ,src_lang:str, tgt_lang:str):
        text_inputs = self.Processor(text = text_input, src_lang=src_lang, return_tensors="pt")
        output_tokens = self.T2TT_Model.generate(**text_inputs, tgt_lang=tgt_lang)
        result  = self.Processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)

        return result
    
    # def Text_2_Speech_Translate(self,text_input ,src_lang:str, tgt_lang:str):
    #     text_inputs = self.Processor(text = text_input, src_lang=src_lang, return_tensors="pt")
    #     output_tokens = self.T2ST_Model.generate(**text_inputs, tgt_lang=tgt_lang)
    #     result  = self.Processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)

    #     return result
    
    # def Speech_2_Text_Translate(self,text_input ,src_lang:str, tgt_lang:str):
    #     text_inputs = self.Processor(text = text_input, src_lang=src_lang, return_tensors="pt")
    #     output_tokens = self.S2TT_Model.generate(**text_inputs, tgt_lang=tgt_lang)
    #     result  = self.Processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)

    #     return result
    
    # def Text_2_Text_Translate(self,text_input ,src_lang:str, tgt_lang:str):
    #     text_inputs = self.Processor(text = text_input, src_lang=src_lang, return_tensors="pt")
    #     output_tokens = self.S2ST_Model.generate(**text_inputs, tgt_lang=tgt_lang)
    #     result  = self.Processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)

    #     return result





