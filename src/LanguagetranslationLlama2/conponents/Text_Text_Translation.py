from transformers import SeamlessM4TForTextToText,SeamlessM4TForSpeechToText,SeamlessM4TForTextToSpeech,SeamlessM4TForSpeechToSpeech,AutoProcessor
import torchaudio
from src.LanguagetranslationLlama2.constants import DIRECTORY,FILENAME
import os
import torch
# import wave
# from io import BytesIO


class Text_Translation:
    def __init__(self): #Model_Tokenizer_config: Model_Tokenizer
        # self.M_T_Config = Model_Tokenizer_config

        model_path = os.path.join(DIRECTORY, FILENAME)
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"

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
        # self.sample_rate = self.S2ST_Model.config.sampling_rate


    def Text_2_Text_Translate(self,text_input ,src_lang, tgt_lang:str):

        try:
            print(self.device)
            self.T2TT_Model.to(self.device)
            text_inputs = self.Processor(text = text_input, src_lang=src_lang, return_tensors="pt").to(self.device)
            output_tokens = self.T2TT_Model.generate(**text_inputs, tgt_lang=tgt_lang).to(self.device)
            result  = self.Processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)
            return result
        except Exception as e:
            raise e
        
    
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
        
    # def wav_to_binaryio(wav_file):
    #     """
    #     This function reads a WAV file and returns its contents as a BytesIO object.

    #     Args:
    #         wav_file (str): Path to the WAV file.

    #     Returns:
    #         BytesIO: Object containing the WAV file data in binary format.
    #     """
    #     with wave.open(wav_file, 'rb') as wav_obj:
    #         # Get WAV parameters
    #         params = wav_obj.getparams()
    #         frames = wav_obj.readframes(params.nframes)  # Read all frames

    #     # Create a BytesIO object and write the WAV data
    #     binary_data = BytesIO()
    #     binary_data.write(frames)

    #     # Reset the cursor to the beginning of the BytesIO object
    #     binary_data.seek(0)
    #     return binary_data    
        

    # def Speech_2_Speech_Translate(self,audio_arrey , tgt_lang:str):
    #     try:
    #         print(f"audio file path {audio_arrey}")
       
    #         audio_sample, audio_sampling_rate = torchaudio.load(audio_arrey)

    #         # Resample the audio if the sampling rate is different from the model's sampling rate
    #         if audio_sampling_rate != self.S2ST_Model.config.sampling_rate:
    #             audio_sample = torchaudio.functional.resample(audio_sample,
    #                                                         orig_freq=audio_sampling_rate,
    #                                                         new_freq=self.S2ST_Model.config.sampling_rate)

    #         # Process the audio inputs
    #         audio_inputs = self.Processor(audios=audio_sample, return_tensors="pt",sampling_rate=self.S2ST_Model.config.sampling_rate).to(self.device)

    #         # Generate speech from the processed audio inputs
    #         audio_array_from_audio = self.S2ST_Model.generate(**audio_inputs, tgt_lang=tgt_lang,spkr_id=7)[0].cpu().numpy().squeeze()

    #         return audio_array_from_audio
    #     except Exception as e:
    #         raise e
   




