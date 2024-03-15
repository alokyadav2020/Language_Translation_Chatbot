from src.LanguagetranslationLlama2.conponents.laguage_translation import Translation



class Translation_Pipelines:
    def __init__(self) -> None:
        pass


    def model_pipeline(self):
        obj = Translation()
        model,tokenizer = obj.load_model()
        # gen_token = obj.generate_token(model=model,tokenizer=tokenizer,text=text)
        return model,tokenizer
    

    def translation_pipeline(self):
        