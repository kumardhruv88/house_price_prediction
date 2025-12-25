document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    const submitBtn = e.target.querySelector('button');
    const resultContainer = document.getElementById('result');
    const priceValue = document.getElementById('priceValue');

    // Loading state
    submitBtn.textContent = 'Calculating...';
    submitBtn.disabled = true;
    resultContainer.classList.add('hidden');

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            priceValue.textContent = result.prediction;
            resultContainer.classList.remove('hidden');
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('An error occurred. Please try again.');
        console.error('Error:', error);
    } finally {
        submitBtn.textContent = 'Predict Price';
        submitBtn.disabled = false;
    }
});
