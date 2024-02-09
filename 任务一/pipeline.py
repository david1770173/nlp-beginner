"""
pipeline is used to load dataset as standard nparrays
the functions in this file are just function prototype, you should never expect to
find just the right one for your case. Instead you choose the one with similar output
and input and modify the code in your own file.

New pipelines should ONLY be added back to this file IF:
the pipeline has a new return type 
OR 
you spend a lot of efforts in adapting existing pipelines and you think it's worth 
risking making the pipeline.py clumsy to save efforts for later use 
"""
import pandas as pd
import numpy as np
def load_bag_of_words():
    """generated by chatgpt 4"""
    # 读取TSV文件
    df = pd.read_csv(r"D:\大学学习\nlp-beginner\任务一\train.tsv.zip", sep='\t')

    # 预处理文本数据：转换为小写
    df['Phrase'] = df['Phrase'].str.lower()

    # 提取情感标签为NumPy数组
    sentiments = np.array(df['Sentiment'].values)

    # 构建词汇表：简化处理，我们仅考虑每个独特单词的出现不进行频率限制
    words = pd.Series(' '.join(df['Phrase']).split()).value_counts().index.tolist()

    # 将词汇表转换为{word: index}的形式
    word_index = {word: i for i, word in enumerate(words)}

    # 初始化词向量矩阵
    word_vectors = np.zeros((len(df), len(word_index)), dtype=np.int8)

    # 填充词向量矩阵
    for i, phrase in enumerate(df['Phrase']):
        for word in phrase.split():
            if word in word_index:
                word_vectors[i, word_index[word]] += 1
    return word_vectors, sentiments    