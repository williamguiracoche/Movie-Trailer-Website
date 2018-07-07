import media
import fresh_tomatoes

# Creating all movie instances. Movie class found in media.py

top_gun = media.Movie(
    "Top Gun",
    "https://imgc.allpostersimages.com/img/posters/top-gun-movie-tom-cruise-and-kelly-mcgillis-80s-poster-print_u-L-F575DB0.jpg?src=gp&w=300&h=375",  # NOQA
    "https://www.youtube.com/watch?v=qAfbp3YX9F0")

apollo_13 = media.Movie(
    "Apollo 13",
    "https://m.media-amazon.com/images/M/MV5BNjEzYjJmNzgtNDkwNy00MTQ4LTlmMWMtNzA4YjE2NjI0ZDg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KtEIMC58sZo")

the_martian = media.Movie(
    "The Martian",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_aviator = media.Movie(
    "The Aviator",
    "https://m.media-amazon.com/images/M/MV5BZTYzMjA2M2EtYmY1OC00ZWMxLThlY2YtZGI3MTQzOWM4YjE3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FebPJlmgldE")

flight = media.Movie(
    "Flight",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQOyXxr0BaYaRUy0krslHpZ2A-OBDev2HhNzbdgTp4oEEuPxzeR",  # NOQA
    "https://www.youtube.com/watch?v=yH7sjSZ85-k")

star_trek = media.Movie(
    "Star Trek",
    "http://www.gstatic.com/tv/thumb/dvdboxart/176379/p176379_d_v8_aa.jpg",
    "https://www.youtube.com/watch?v=SyJszxnJydA")

independence_day = media.Movie(
    "Independence Day",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Independence_day_movieposter.jpg/220px-Independence_day_movieposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=RfJgT89hEME")

flyboys = media.Movie("Flyboys",
    "https://lh3.ggpht.com/9bwpk6vt2_OY35Kg2pKNVO8myD80KLpe0_20CYg5Q54SzF9Keaw2h9nRC8zr82mH1SU=w200-h300",  # NOQA
    "https://www.youtube.com/watch?v=qhKnuKFEKcA")

interstellar = media.Movie(
    "Interstellar",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1NMxxfM9mYM")

guardians = media.Movie(
    "Guardians of the Galaxy",
    "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=d96cjJhvlMA")

star_wars = media.Movie(
    "Star Wars",
    "https://is2-ssl.mzstatic.com/image/thumb/Video6/v4/61/16/ce/6116cec2-d2e8-de26-f80d-38a1685d04b8/source/1200x630bb.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1g3_CFmnU7k")

avatar = media.Movie(
    "Avatar",
    "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Put all of the movies into a list
movies = [
    top_gun, apollo_13, the_martian, the_aviator, flight, star_trek,
    independence_day, flyboys, interstellar, guardians, star_wars, avatar]

# all open_movies_page function from fresh_tomatoes to create the website
fresh_tomatoes.open_movies_page(movies)
