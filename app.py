from app import app, db
from app.models import Favorite

app.config["SECRET_KEY"] = "sratatata"

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Favorite": Favorite,
    }
    
if __name__ == "__main__":
    app.run(debug=True)