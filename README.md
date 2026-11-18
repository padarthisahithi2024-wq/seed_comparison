# 🌱 Seed Comparison and Smart Seed Recommendation System

## About the Project

The Seed Comparison and Smart Seed Recommendation System is a web-based application that helps users compare different seeds and find suitable seeds based on soil type, season, and water requirements.

The application uses Python Flask for the backend and Supabase as the database.

## Features

- **View Seeds:** Display available seed details from the database.
- **Compare Seeds:** Select and compare multiple seeds.
- **Comparison Results:** View seed information side by side.
- **Smart Seed Recommendation:** Get seed recommendations based on selected soil type, season, and water requirement.
- **Supabase Integration:** Store and retrieve seed information.
- **User-Friendly Interface:** Simple and responsive website design.

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- Supabase
- GitHub

## Project Structure

```text
seed_comparison/
│
├── app.py
├── .env
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── compare.html
│   ├── results.html
│   └── recommend.html
│
└── static/
    ├── style.css
    └── script.js
```

## Database

This project uses Supabase as its database.

The `seeds` table contains information such as:

- Seed name
- Crop type
- Soil type
- Season
- Water requirement
- Duration
- Expected yield

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd seed_comparison
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the main project folder.

Add your own Supabase project credentials:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

Never upload your actual API key or `.env` file to GitHub.

### 7. Run the application

```bash
python app.py
```

Open the local website in your browser at:

```text
http://127.0.0.1:5000
```

## How the Project Works

1. The application retrieves seed information from Supabase.
2. Users can view the available seeds.
3. Users select seeds to compare their details.
4. The application displays the comparison results.
5. Users can enter soil, season, and water requirements.
6. The recommendation feature finds matching seeds from the database.

## Future Improvements

- Add more seed varieties.
- Improve recommendation accuracy.
- Add user login and registration.
- Add charts for seed comparison.
- Deploy the application online.

## Conclusion

This project provides a simple way to compare seeds and identify suitable options using database-driven information and a rule-based recommendation system.