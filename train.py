from email.policy import strict
import json
from underthesea import *
import random

with open('data.json', 'r', encoding='utf8', errors='ignore') as f:
    data = json.load(f, strict="False")
    
remove = ['cậu', 'tớ', 'tao', 'mày', 'anh', 'chị', 'có', 'không', 'bị', 'gì', 'thì', 'được', "quá"]

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

# tìm tỉ lệ phù hợp nhất

def get_respond(question):
    rate_calc = []
    question = tokenize(stem(question))
    for intent in data['intents']:
        rate = 0
        label = data['intents'].index(intent)
        for word in question:
            if word in keys[label]:
                rate += 1  
            if word in intent['patterns']:
                rate + 0.25
        rate_calc.append(rate)            
        	
    max_value = max(rate_calc)	
    label = rate_calc.index(max_value)
    rand = random.randint(0,len(data['intents'][label]['responses'])-1)
    return data['intents'][label]['responses'][rand]

