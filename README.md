# Spanish Translator Web App

This is a full-stack web application that shows a **Spanish word of the day**, lets you get a **random word**, and also allows you to **search** for the English meaning of any Spanish word. It uses:

- **FastAPI** for the backend (Python)
- **HTML/CSS/JavaScript** for the frontend
- **Merriam-Webster Spanish-English Dictionary API** for real-time translations
- A local `.txt` file with 15,000 Spanish words for random and daily word selection

I built this project while learning about web development, APIs, and full-stack app structure. This is a work-in-progress learning app.

---

## Video Demo

https://drive.google.com/file/d/1T15ZNICszUwQ0QFwluzRMd4x4fA4Fxz9/view?usp=sharing

**Note: The project demo starts at 9m:30s of the video**

---
## Github Link



---
##  Features

- Displays a consistent “Word of the Day” that changes only once per day.
- Lets you get a totally random Spanish word with its translation.
- Search any Spanish word and get its English translation instantly.
- Logs errors and debugging info to a file for easy tracing.

---

##  How to Run It Locally

This project is divided into two parts:

```

spanish_word_api/
├── backend/     → FastAPI backend
├── frontend/    → HTML, CSS, JS frontend

````

### Backend Setup (FastAPI)

1. **Navigate to the backend folder:**

```bash
cd spanish_word_api/backend
````

2. **Create and activate a virtual environment:**

```bash
python3 -m venv spanishwebapp
source spanishwebapp/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your API key:**

Create a `.env` file in `backend/`:

```
api_key=your_api_key_here
word_source='api' or 'local'
```

5. **Run the FastAPI server:**

```bash
uvicorn app.main:app --reload
```

The backend will now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Frontend Setup

1. **Navigate to the frontend folder:**

```bash
cd ../frontend
```

2. **Start a local server:**

You can use Python’s built-in HTTP server:

```bash
python3 -m http.server 8001
```

Now open your browser and go to:

```
http://localhost:8001
```

> The frontend will send requests to `http://localhost:8000`, so make sure your backend is running!

---

## Configuration Notes

* The app reads environment variables from `.env` using Pydantic.
* Words are loaded from `data/spanish_words.txt` (15,000 common Spanish words).
* Logs are stored in `backend/logs/app.log`.
* CORS is enabled in FastAPI to allow the frontend and backend to communicate across different ports (8000 for backend, 8001 for frontend).

---

## Endpoints (Backend)

| Method | Route               | Description                      |
| ------ | ------------------- | -------------------------------- |
| GET    | `/word_of_the_day`  | Returns today's consistent word  |
| GET    | `/random`      | Returns a completely random word |
| GET    | `/translate/{word}` | Translates any Spanish word      |

---

## What I Learned

* How to structure a full-stack web app project
* Using FastAPI for building APIs
* Fetching data from external APIs (Merriam-Webster)
* Dynamically updating the UI with JavaScript
* How to use `.env`, `logging`, and handle API errors gracefully
* CORS, HTTP status codes, and frontend-backend communication

---

## Future Improvements

* Add audio pronunciation for each word
* Show part of speech (noun, verb, etc.)
* Implement DataBase and Flashcard like feature

---
