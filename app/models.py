from app import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=True, unique=True)

    def __str__(self):
        return f"<Favorite {self.movie_id}>"