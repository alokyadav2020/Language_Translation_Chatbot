from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


class Translation:
    def __init__(self) -> None:
        pass



    def load_model(self,model_path):
        model = MBartForConditionalGeneration.from_pretrained(model_path)
        tokenizer = MBart50TokenizerFast.from_pretrained(model_path, src_lang="en_XX")

        return model,tokenizer
    

    def generate_token(self,text,tokenizer,model):
        model_inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(
                          **model_inputs,
                            forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
                                         )
        
        return generated_tokens
    

    def translate(self,generated_tokens,tokenizer):
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        return translated_text