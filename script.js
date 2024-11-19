document.getElementById('testForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const urlInput = document.getElementById('url');
    const url = urlInput.value;

    fetch('/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `url=${encodeURIComponent(url)}`
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            // Show results section
            const resultsSection = document.getElementById('results');
            const resultsContent = document.getElementById('resultsContent');
            const reportUrl = document.getElementById('reportUrl');
            const reportResults = document.getElementById('reportResults');

            resultsContent.innerHTML = `
                <p><strong>URL:</strong> ${data.url}</p>
                <ul>
                    ${data.vulnerabilities.map(vuln => `<li>${vuln.type}: ${vuln.status}</li>`).join('')}
                </ul>
            `;

            // Populate hidden fields for report
            reportUrl.value = data.url;
            reportResults.value = JSON.stringify(data);

            resultsSection.classList.remove('hidden');
        })
        .catch(error => console.error('Error:', error));
});
