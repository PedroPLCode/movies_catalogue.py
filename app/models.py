from app import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=True, unique=True)
    movie_title = db.Column(db.String(100), index=True)

    def __str__(self):
        return f"<Favorite: movie_title: {self.movie_title}, movie_id: {self.movie_id}>"