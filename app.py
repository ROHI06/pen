from flask import Flask, request, render_template, jsonify, make_response
from fpdf import FPDF

app = Flask(__name__)

# Home route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get('url')  # Get URL from the form
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Simulate penetration testing results
    results = {
        'url': url,
        'vulnerabilities': [
            {'type': 'SQL Injection', 'status': 'Not Found'},
            {'type': 'XSS', 'status': 'Detected'},
            {'type': 'CSRF', 'status': 'Not Found'},
            {'type': 'Open Redirect', 'status': 'Not Found'}
        ]
    }
    return jsonify(results)

# Route to generate a PDF report
@app.route('/download-report', methods=['POST'])
def download_report():
    url = request.form.get('url')
    results = request.form.get('results')  # Expecting results in JSON format
    if not url or not results:
        return 'Invalid data', 400

    results = eval(results)  # Convert string back to dictionary (for demo purposes)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to the PDF
    pdf.cell(200, 10, txt="Penetration Testing Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"URL: {url}", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Vulnerabilities Found:", ln=True)
    pdf.ln(5)
    for vuln in results['vulnerabilities']:
        pdf.cell(200, 10, txt=f"- {vuln['type']}: {vuln['status']}", ln=True)

    # Output PDF
    response = make_response(pdf.output(dest='S').encode('latin1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response

if __name__ == '__main__':
    app.run(debug=True)
