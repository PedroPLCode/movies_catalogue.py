[ -d "$HOME/.local/bin" ] && PATH="$HOME/.local/bin:$PATH"
export FLASK_APP=app.py
export PATH
export FLASK_ENV=development
export TMDB_API_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzNlYTA2YjZmZmYyOGI1MmNhMGEwYjhlNzMxNTkxMSIsInN1YiI6IjY1Y2JhMzZmYTA2ZWZlMDE2Mzc2NmI1MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._3lmM-wYIi8iokibDPS648HdFWVzLZDVKXzzigrsgzw"
flask run