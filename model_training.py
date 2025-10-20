import pickle
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline


with open("reviews", "rb") as f:
    loaded_reviews = pickle.load(f)

tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

all_words = []
for review, cat in loaded_reviews:
    tokens = tokenizer.tokenize(review)
    for word in tokens:
        if word not in stop_words:
            all_words.append(word.lower())

all_words = nltk.probability.FreqDist(all_words)

#print(len(list(all_words.keys())))

filtered_vocab = [w for w in all_words if all_words[w] > 3]
#print(len(filtered_vocab))
#all_words.plot(20, title="Top 20 Most Common Words")
#plt.show()

def find_features(document):
    words = set(document)
    features = {}
    for w in filtered_vocab:
        features[w] = (w in words)
    return features

feature_set = []
for review, cat in loaded_reviews:
    tokens = tokenizer.tokenize(review)
    feature_set.append((find_features(tokens), cat))

training_set = feature_set[:2200]
testing_set = feature_set[2200:]

classifier = SklearnClassifier(MultinomialNB())
classifier.train(training_set)
X = [rew for rew, cat in feature_set]
y = [cat for rew, cat in feature_set]
acc = nltk.classify.accuracy(classifier, testing_set)

pipe = make_pipeline(DictVectorizer(sparse=True), MultinomialNB())


print("MultinomialNB accuracy: ", acc)

# cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# results = cross_validate(pipe, X, y, cv=cv, scoring='accuracy', return_train_score=False)
#
# print("Cross-validation scores:", results['test_score'])
# print("Mean accuracy: ", np.mean(results['test_score']))
# print("Std deviation: ", results['test_score'])
#

test_reviews = [
    "This might be the best movie I have seen so far!",
    "It was so boring and slow, I almost fell asleep.",
    "I have seen worse, but the ending was kinda disappointing.",
    "Waste of time. It was horrible!",
    "One of the all time greats! It was fantastic."
]

for review in test_reviews:
    tokens = tokenizer.tokenize(review.lower())
    features = find_features(tokens)
    prediction = classifier.classify(features)
    print(f"Review: {review}\nPrediction: {prediction}\n")
