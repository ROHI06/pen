from flask import Flask, request, jsonify, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def penetration_test():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify(success=False, error="Invalid URL")

    # Simulated results (replace with real pentesting logic)
    results = f"""
    <ul>
        <li>Scanning website: {url}</li>
        <li>Open Ports: 80, 443</li>
        <li>SSL Validity: Pass</li>
        <li>SQL Injection Test: No vulnerabilities found</li>
        <li>XSS Test: Vulnerabilities found in input field 'search'</li>
    </ul>
    """
    with open('report.pdf', 'w') as f:
        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()
        pdf.cell(200, 10, txt="Penetration Test Report", ln=True, align='C')
        pdf.multi_cell(0, 10, f"Results for {url}:\n" + results)
        pdf.output("report.pdf")

    return jsonify(success=True, results=results)

@app.route('/download', methods=['GET'])
def download_report():
    path = "report.pdf"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return jsonify(success=False, error="No report found")

if __name__ == '__main__':
    app.run(debug=True)
