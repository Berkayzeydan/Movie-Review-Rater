# Movie-Review-Rater
A movie review sentiment analysis project that collects reviews via API calls from the TMDb API and uses NLTK and scikit-learn to preprocess and classify movie reviews as positive or negative.

## Data Source
TMDb API- https://www.themoviedb.org

## Accuracy
Single split accuracy: ~85.9%
Cross-validation mean accuracy: ~88% ± 1.2

## Example Predictions
Review: This might be the best movie I have seen so far!
Prediction: positive

Review: It was so boring and slow, I almost fell asleep.
Prediction: negative

Review: I have seen worse, but the ending was kinda disappointing.
Prediction: negative

Review: Waste of time. It was horrible!
Prediction: negative

Review: One of the all time greats! It was fantastic.
Prediction: positive

## Possible Improvements
Collecting more and longer reviews 

Using either lemmatizinr or stemming to unify similar terms

Gaining deeper insight based on results 

Experimenting with different models 

Refactoring the code for better readability and maintainability.
