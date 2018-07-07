import webbrowser
# Create movie class


class Movie():
    """This class allows you to define a movie and store its title,
    poster image link and youtube trailer link"""

    # Each movie object will store the title, poster image and youtube trailer
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Opens trailer using webbrowser.open
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
