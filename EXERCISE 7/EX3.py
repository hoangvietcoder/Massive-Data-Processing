import nltk

from nltk.tokenize import word_tokenize
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

nltk.download('punkt')

sentences = ["Đừng yêu em vì em là thuốc phiện. Nghiện vào rồi là không bỏ được đâu."]
tokenized_sent = []
for s in sentences:
    tokenized_sent.append(word_tokenize(s.lower()))


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_sent)]
model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, epochs=100)

test_doc = word_tokenize("I had hot dogs and hamburgers".lower())
test_doc_vector = model.infer_vector(test_doc)
result = model.dv.most_similar(positive=[test_doc_vector])

print(result)

with open("kq.txt", "w", encoding="utf-8") as kq:
    kq.writelines(str(result))
