from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/scrape-social', methods=['POST'])
def scrape_social():
    data = request.json
    platform = data.get('platform')
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # Example: Scrape page title
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"

        return jsonify({"platform": platform, "url": url, "title": title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/find-person', methods=['POST'])
def find_person():
    data = request.json
    company = data.get('company')
    job_title = data.get('job_title')

    # Dummy Data for Demo
    employees = [
        {"name": "John Doe", "email": "john@company.com", "job_title": "Manager"},
        {"name": "Jane Smith", "email": "jane@company.com", "job_title": "Engineer"}
    ]

    filtered = [emp for emp in employees if emp['job_title'] == job_title]
    return jsonify(filtered)

@app.route('/export', methods=['POST'])
def export_data():
    data = request.json.get('data')
    df = pd.DataFrame(data)
    file_path = 'output.xlsx'
    df.to_excel(file_path, index=False)
    return jsonify({"message": "Data exported successfully", "file": file_path})

if __name__ == '__main__':
    app.run(debug=True)
