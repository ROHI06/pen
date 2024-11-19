document.getElementById('testForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const url = document.getElementById('urlInput').value;

    // Fetch results from the server
    const response = await fetch('/test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
    });

    const data = await response.json();

    if (data.success) {
        document.getElementById('resultContent').innerHTML = data.results;
        document.querySelector('.results').classList.remove('hidden');
        document.querySelector('.details').classList.remove('hidden');
    } else {
        alert('Error: ' + data.error);
    }
});

function toggleResults() {
    const details = document.querySelector('.details');
    details.classList.toggle('hidden');
}

document.getElementById('downloadButton').addEventListener('click', function () {
    fetch('/download').then(response => {
        response.blob().then(blob => {
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'Penetration_Test_Report.pdf';
            link.click();
        });
    });
});
