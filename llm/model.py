import torch
from tqdm.notebook import tqdm
tqdm.pandas()
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from spellchecker import SpellChecker


# Load Model and Tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
PAD_TOKEN = tokenizer(tokenizer.pad_token)['input_ids'][0]
model = AutoModelForCausalLM.from_pretrained(f'./v{ver}_final_model')  # Use this to load our fine tuned model

# Evaluation
text_generator = pipeline('text-generation', tokenizer=tokenizer, model=model)
chunk_size = 128
buffer = 8
question = 'What are the moods evoked by the following song excerpt?'
BLACKLIST = [
    'ive',
    'ersatz',
    'ery',
    'e',
    'no',
    'ado',
    'tri',
    'ute',
    'ric',
    '"',
    'ious',
    'izzy',
    'su'
]


spell = SpellChecker()
def check(word: str) -> bool:
    if word == spell.correction(word) and word not in BLACKLIST:
        return True
    else:
        return False


def flatten_array(array: list):
    tags_array = []
    for i in array:
        tags_array += i
    return tags_array
    

def tags_for_excerpt(tokens: list) -> str:
    # tokens = tokenizer(excerpt)['input_ids']
    excerpt = tokenizer.decode(tokens)
    output = text_generator(excerpt, 
                         max_length=len(tokens) + TOKENS_TO_GENERATE)[0]['generated_text']
    response = output[output.rfind('A: ') + 3:]
    response_tags = response.split(', ')
    response_tags = [i.strip(', \nÂ') for i in response_tags]
    response_tags = list(filter(check, response_tags))
    return response_tags


def select_tags(tags: list, num: int):
    unique_tags, counts = np.unique(tags, return_counts=True)
    
    freq_diffs = []
    for i in range(len(unique_tags)):
        if unique_tags[i] in tag_map.keys():
            freq_diffs.append(counts[i] / len(tags) - tag_map[unique_tags[i]])
        else:
            freq_diffs.append(UNK_TAG_WEIGHT)
    sorted_tags = unique_tags[np.argsort(freq_diffs)][::-1]
    return list(sorted_tags[:num])


def format_lyrics(lyrics):
    lyrics_lst = lyrics.split("\n")
    result = [[lyrics_lst[0], 1]]

    for i in range(len(lyrics_lst) - 1):
        if lyrics_lst[i] != lyrics_lst[i+1] or lyrics_lst[i+1] == '':
            result.append([lyrics_lst[i+1], 1])
        else:
            result[-1][1] += 1

    result2 = [i[0] for i in result]
    for i in range(len(result)):
        if result[i][1] > 1:
            result2[i] += f" (x{result[i][1]})"
    return '\n'.join(result2)


# generates tags for a single song
def gen_tags(lyrics: str, num_tags: int) -> list[list[str]]:
    lyrics = format_lyrics(lyrics)
    chunks = process_lyrics(lyrics)
    result = [tags_for_excerpt(i) for i in chunks]
    
    tags_array = flatten_array(result)
    
    return select_tags(tags_array, num_tags)


def process_user(lyrics_arr):
    return select_tags(flatten_array(map(lambda i: gen_tags(i, 8), lyrics_arr)), 10)


def high_fidelity_gen_tags(lyrics, num_tags):
    all_tags = []
    for i in range(10):
        lyrics = format_lyrics(lyrics)
        chunks = process_lyrics(lyrics)
        result = [tags_for_excerpt(i) for i in chunks]

        tags_array = flatten_array(result)
        all_tags += tags_array
    return select_tags(all_tags, num_tags)