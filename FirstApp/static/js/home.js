function displayTable(category) {
    document.getElementById('display_btn').addEventListener('click', function () {
        fetch("{% url 'display_data_from_db' %}")
            .then(response => response.text())
            .then(data => {
                document.getElementById('result').innerText = data;
            })
        // .catch(error => console.error('Error:', error));
    });
}


// Function to set up button listener
function setupButtonListener(ButtonName, targetElementId, urlPrefix) {
    document.querySelectorAll(`input[name="${ButtonID}"]`).forEach((radio) => {
        radio.addEventListener('change', function () {
            // Get the selected radio button ID
            const category = this.id;

            // Send the selected ID to the server
            fetch(`${urlPrefix}/${category}/`)
                .then(response => response.text())
                .then(html => {
                    // Replace the content of the page with the fetched data
                    document.getElementById(targetElementId).innerHTML = html;
                })
                .catch(error => console.error('Error:', error));
        });
    });
}

// Call the function with the appropriate parameters
setupButtonListener('categoryBTNs', 'data-display', '/display');
