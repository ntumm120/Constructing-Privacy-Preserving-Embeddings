from transformers import AutoTokenizer

MODEL_NAME = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

class Example:
    def __init__(self, sentence, label, metadata = None):
        self.sentence = sentence
        self.label = label
        self.sentence = sentence
        self.p_sentence = tokenizer(sentence, truncation=True).input_ids
        
        self.metadata = metadata
    
    def get_label(self):
        return self.label
    
    def get_tokenized(self):
        return self.p_sentence

    def get_sentence(self):
      return self.sentence
    
    def get_aux_labels(self):
        return self.metadata
    
    def get_training_example(self):
        return self.p_sentence, self.label
    
    def get_aux_training(self):
        return self.p_sentence, self.metadata

def get_hidden_size():
  return len(tokenizer)
