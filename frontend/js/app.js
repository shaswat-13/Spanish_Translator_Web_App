const API_BASE_URL = "http://127.0.0.1:8000"; // localhost URL for the backend

// get word of the day from backend
async function getWordOfTheDay() {
  try {
    const res = await fetch(`${API_BASE_URL}/word_of_the_day`);
    const data = await res.json();
    document.getElementById("wotd-spanish").textContent = data.spanish;
    document.getElementById("wotd-english").textContent = data.english;
  } catch (error) {
    alert("Failed to fetch word of the day.");
  }
}

// get random word from backend
async function getRandomWord() {
  try {
    const res = await fetch(`${API_BASE_URL}/random/`);
    const data = await res.json();
    document.getElementById("random-spanish").textContent = data.spanish;
    document.getElementById("random-english").textContent = data.english;
  } catch (error) {
    alert("Failed to fetch random word.");
  }
}

// search for the translation of the typed word
async function searchWord() {
  const word = document.getElementById("search-input").value.trim();
  if (!word) return;

  try {
    const res = await fetch(`${API_BASE_URL}/translate/${word}`);
    const data = await res.json();
    document.getElementById("search-english").textContent = data.english;
  } catch (error) {
    alert("Translation failed.");
  }
}

// when the file loads, get the word of the day and make the container visible
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".container").style.opacity = 1;
  getWordOfTheDay();
});
