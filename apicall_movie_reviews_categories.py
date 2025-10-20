from requests import get
from dotenv import load_dotenv
import os
import pickle


load_dotenv()

base_url = "https://api.themoviedb.org/3"
api_key = os.environ.get("API_KEY")

#get ids of movies based on the amount you input as a list
def get_movie_ids(movie_amount:int):
    movie_names = []
    page = int(movie_amount/20)
    if movie_amount%20 != 0:
        page += 1
    for a in range(page):
        params = {"api_key": api_key, "page":a+1}
        response = get(url=f"{base_url}/movie/popular", params=params).json()
        for movie in response["results"]:
            movie_names.append(movie['id'])

    movie_names = movie_names[0:movie_amount]
    return movie_names

# go through a list of movie ids and get the reviews available and give them labels as positive or
# negative based on the ratings of them in the end return a list of tuples
def get_label_reviews(id_list:list):
    revs = []
    for movie_id in id_list:
        params = {"api_key": api_key}
        response = get(url=f"{base_url}/movie/{movie_id}/reviews", params=params)
        if response.status_code != 200:
            print("dogru deil")
            exit()
        results = response.json()['results']

        for person in results:
            word_count = len(person['content'].split())
            if word_count > 100:
                continue

            if person["author_details"]["rating"] is None:
                continue
            elif person["author_details"]["rating"] <= 4:
                revs.append((person['content'], "negative"))
            elif person["author_details"]["rating"] >= 6:
                revs.append((person['content'], "positive"))
            else:
                continue

    return revs

# call the functions
ids = get_movie_ids(movie_amount=8000)
reviews = get_label_reviews(ids)
print("Sample_size: ", len(reviews))
# dump on the reviews file
with open('reviews', 'wb') as fp:
    pickle.dump(reviews, fp)
