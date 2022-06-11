import json
from underthesea import *
import random

with open('data.json', 'r', encoding='utf8', errors='ignore') as f:
    data = json.load(f)
    
remove = ['cậu', 'tớ', 'tao', 'mày', 'anh', 'chị', 'có', 'không', 'bị', 'gì', 'thì', 'được']

# xóa bỏ những từ không cần thiết + tách từ

def tokenize(sentence):
    sentence = word_tokenize(sentence)
    for word in remove:
        if word in sentence:
            sentence.remove(word)
    return sentence

# quy đổi câu về chữ thường + loại bỏ các ký tự đặc biệt

def stem(sentence):
    sentence = sentence.lower()
    new_string = ''
    for char in sentence:
        if (char.isalpha() == 1 or char.isnumeric() == 1 or char == ' '): 
            new_string = new_string + char
    return new_string

# tính tỉ lệ xuất hiện của câu hỏi

keys = []

def init():
    for intent in data['intents']:
        row = []
        for key in intent['keyword']:
            key = word_tokenize(key)
            row.extend(key)
        keys.append(row)

def best_match(question):
    rate_calc = []
    question = tokenize(stem(question))
    print(question)
    i = 0
    for intent in data['intents']:
        rate = 0
        i += 1
        for keywords in intent['keyword']:	
            for words in question:
                if words in keywords:
                    rate += 1
                    break
        rate_calc.append(rate)
    
    max_value = max(rate_calc)
    if max_value < 1:
        return data['intents'][len(data['intents'])-1]['responses'][0]
    label = rate_calc.index(max_value)
    rand = random.randint(0,len(data['intents'][label]['responses'])-1)
    return data['intents'][label]['responses'][rand]
      


if __name__ == "__main__":
    init()
    while True:
        question = input()
        print(best_match(question))