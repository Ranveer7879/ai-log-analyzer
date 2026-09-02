async function analyzeLogs() {

    const fileInput = document.getElementById("logFile");
    const file = fileInput.files[0];

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    const resultsBody = document.getElementById("resultsBody");

    // Check file
    if (!file) {
        error.textContent = "Please select a CSV file.";
        return;
    }

    // Clear previous data
    error.textContent = "";
    resultsBody.innerHTML = "";

    loading.style.display = "block";

    // Create form data
    const formData = new FormData();

    formData.append("file", file);

    try {

        // Send CSV to Flask API
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // Hide loading
        loading.style.display = "none";

        // API error
        if (!response.ok) {
            error.textContent = data.error || "Something went wrong.";
            return;
        }

        // Update dashboard
        document.getElementById("totalLogs").textContent =
            data.total_logs;

        const anomalies = data.results.filter(
            item => item.severity !== "NORMAL"
        ).length;

        const critical = data.results.filter(
            item => item.severity === "CRITICAL"
        ).length;

        document.getElementById("anomalies").textContent =
            anomalies;

        document.getElementById("critical").textContent =
            critical;


        // Add results to table
        data.results.forEach(item => {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${item.timestamp}</td>
                <td>${item.level}</td>
                <td>${item.message}</td>
                <td>${item.cpu}%</td>
                <td>${item.ram}%</td>
                <td>${item.severity}</td>
                <td>${item.anomaly_score}</td>
            `;

            resultsBody.appendChild(row);
        });

    } catch (err) {

        loading.style.display = "none";

        error.textContent =
            "Unable to connect to the server.";

        console.error(err);
    }
}