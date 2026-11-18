
import os
from pathlib import Path

from flask import Flask, render_template, request
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from project folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

# Create Flask application
app = Flask(__name__)

# Get Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()

# Connect to Supabase
supabase = None

if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(
            SUPABASE_URL,
            SUPABASE_KEY
        )
        print("Supabase client initialized successfully!")

    except Exception as error:
        print("Supabase initialization failed:", error)

else:
    print("Missing Supabase credentials. Check your .env file.")


# Fetch all seeds from Supabase
def get_seeds():

    if supabase is None:
        return [], "Supabase is not configured. Please check your .env file."

    try:
        response = (
            supabase.table("seeds")
            .select("*")
            .order("seed_name")
            .execute()
        )

        return response.data or [], None

    except Exception as error:
        return [], str(error)


# Home page
@app.route("/")
def home():

    seeds, error = get_seeds()

    return render_template(
        "index.html",
        seeds=seeds,
        error=error
    )


# Compare page
@app.route("/compare")
def compare():

    seeds, error = get_seeds()

    return render_template(
        "compare.html",
        seeds=seeds,
        error=error
    )


# Display comparison results
@app.route("/results", methods=["POST"])
def results():

    selected_ids = request.form.getlist("seed_ids")

    # Check whether at least two seeds are selected
    if len(set(selected_ids)) < 2:

        seeds, error = get_seeds()

        return render_template(
            "compare.html",
            seeds=seeds,
            error="Please select at least two seeds."
        )

    # Check Supabase connection
    if supabase is None:
        return "Supabase is not configured. Check your .env file.", 500

    try:
        response = (
            supabase.table("seeds")
            .select("*")
            .in_("id", selected_ids)
            .execute()
        )

        selected_seeds = response.data or []

        if len(selected_seeds) < 2:
            return "Please select at least two valid seeds.", 400

        return render_template(
            "results.html",
            seeds=selected_seeds
        )

    except Exception as error:
        return f"Could not compare seeds: {error}", 500


# Test Supabase connection
@app.route("/test-supabase")
def test_supabase():

    if supabase is None:
        return {
            "error": "Supabase credentials are missing. Check your .env file."
        }, 500

    try:
        response = (
            supabase.table("seeds")
            .select("*")
            .execute()
        )

        return {
            "message": "Supabase connected successfully!",
            "total_seeds": len(response.data or []),
            "seeds": response.data or []
        }

    except Exception as error:
        return {
            "error": str(error)
        }, 500


# Start Flask application
if __name__ == "__main__":
    app.run(debug=True)
