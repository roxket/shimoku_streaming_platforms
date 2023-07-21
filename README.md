# Shimoku Streaming Platform Dashboard

## Context

In today's digital age, the landscape of entertainment has undergone a remarkable transformation. With the rise of streaming platforms, our options for indulging in captivating series and movies have expanded like never before. Gone are the days of being bound by rigid television schedules or limited movie selections at local theaters. Now, we have the freedom to explore a vast realm of content at our fingertips.

Streaming platforms such as Netflix, Amazon Prime Video, Hulu, and Disney+ have revolutionized the way we consume visual media. They offer an extensive library of series and movies, spanning across genres and catering to diverse tastes. From gripping dramas and thrilling action adventures to side-splitting comedies and thought-provoking documentaries, these platforms deliver an immersive and personalized viewing experience.

## Objectives

Analyze and filter series and movies data using the Shimoku Platform and its library on the basis of an open question or free approach, in order to create graphs with results.

## Datasets

You will have to work with these two datasets:

**all_titles** includes the next parameters:
- id: ID for the title.
- title: Name of the movie or show.
- type: indicates if it is a movie or a show.
- description: brief synopsis of the title.
- release year: Year where the movie/show was first released.
- age_certification: certification type of age limitation, if any.
- runtime: duration of the full movie or duration of each show episode.
- genres: list of main movie or show genres.
- production_countries: list of countries where the title was produced.
- seasons: number of seasons of the show.
- imdb_id: identifier of the Internet Movie DataBase (IMDB) dataset.
- imdb_score: average public rating of the title in IMDB.
- imdb_votes: number of votes used to compute the imdb_score field.
- tmdb_popularity: popularity score of the title on the The Movie DataBase (TMDB) platform.
- tmdb_score: average rating of the title in TMDB.
- streaming: name of the streaming service listing the film.

**all_credits** includes the next parameters:
- person_id: identifier of the person doing the role.
- id: ID for the title (same ID used on all_titles.csv).
- name: name of the person doing the role.
- character: name of the character in the title, if any.
- role: indicates if the person has the role actor or a director.

## Proposal Layout Design

These dashboards serve as streaming platform analysis with the Shimoku SDK.

### Titles Dashboard

- Total titles: An indicator displaying the number of titles.
- Total titles hours: An indicator displaying the total hours of titles.
- Mean IMDb score: An indicator displaying the average IMDb score.
- Popular Genres: A rose chart displaying the popular genres.
- Popular Movies: A horizontal bar chart displaying the most popular movies.
- Series Trend: A line chart displaying the number of series productions over time.

        
### Credits Dashboard

- Total actors: An indicator displaying the total number of actors in the database.
- Total directors: An indicator displaying the total number of directors in the database.
- Top 5 actors: A horizontal bar chart displaying the most frequently appearing actors.
- Top 5 directors: A horizontal bar chart displaying the most frequently appearing directors.
- Director Analysis: A horizontal bar chart for comparing the average ratings of different directors.
- Actor/Actress Influence: A horizontal bar chart for comparing the ratings of movies featuring different actors or actresses.


