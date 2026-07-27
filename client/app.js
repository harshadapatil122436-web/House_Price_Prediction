const API_BASE = 'https://house-price-prediction-84hh.onrender.com';

const locationSelect = document.getElementById('location');
const statusLine = document.getElementById('status-line');
const predictBtn = document.getElementById('predict-btn');
const resultBox = document.getElementById('result');
const resultValue = document.getElementById('result-value');

// This part fills the dropdown with location names
fetch(`${API_BASE}/get_location_names`)
  .then(res => res.json())
  .then(data => {
    const locations = data.locations || [];
    locationSelect.innerHTML = '';
    locations.forEach(loc => {
      const opt = document.createElement('option');
      opt.value = loc;
      opt.textContent = loc;
      locationSelect.appendChild(opt);
    });
  });

// This part runs when you click "Estimate Price"
predictBtn.addEventListener('click', () => {
  const location = locationSelect.value;
  const sqft = document.getElementById('sqft').value;
  const bhk = document.getElementById('bhk').value;
  const bath = document.getElementById('bath').value;

  const formData = new URLSearchParams();
  formData.append('total_sqft', sqft);
  formData.append('location_name', location);
  formData.append('bhk_price', bhk);
  formData.append('bath_price', bath);

  fetch(`${API_BASE}/predict_home_price`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData.toString()
  })
    .then(res => res.json())
    .then(data => {
      resultValue.innerHTML = data.estimated_price + ' lakhs';
      resultBox.classList.add('show');
    });
});
