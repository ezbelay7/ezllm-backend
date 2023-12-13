import sys
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_text(input_text):
    # Initialize the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

    # Encode the input text and generate a response
    inputs = tokenizer([input_text], return_tensors='pt', padding=True, truncation=True, max_length=512)
    reply_ids = model.generate(**inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode and return the output text
    return tokenizer.decode(reply_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    user_input = sys.argv[1]  # Get user input from command-line argument
    print(generate_text(user_input))
