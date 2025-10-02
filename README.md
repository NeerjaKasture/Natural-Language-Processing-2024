# Natural-Language-Processing-2024

## Assignment 1

Contains code to scrape urdu words from the following sources:
- BBC Urdu
- Daily Jang
- Hindustan Express
- Hindustan Times
- Siasat
- The Wire Urdu
- Wikipedia
- News 18

It also has the code for deduplication using MinHash and SimHash, and data cleaning using a manually selected 'Negative Words' list.

The cleaned data can be found on Huggingfaces. [link](https://huggingface.co/datasets/snehagautam/nlp_webscraping/tree/main)

## Assignment 2

Contains code used to train tokenizer ( ByteLevelBPETokenizer, SentencePieceBPETokenizer) and train the model (LlamaForCausalLM architecture) from scratch using Google Colab GPUs.

The datasets and model can be found on HuggingFaces : [Datasets Tokenized](https://huggingface.co/datasets/NeerjaK/Urdu_Model/tree/main), [Model trained](https://huggingface.co/NeerjaK/Urdu_Model/tree/main)

## Assignment 3

Contains code used to finetune Llama-3.2-1B model on the SST and SQUAD datasets. The tokenized datasets can be found on Hugginfaces [link](https://huggingface.co/datasets/NeerjaK/NLP-Assignment3/tree/main)
