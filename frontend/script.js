const API_URL = "http://127.0.0.1:5000";


// Load metrics from backend
async function loadMetrics() {

    try {

        const response = await fetch(`${API_URL}/api/metrics`);

        const data = await response.json();

        if (data.status !== "success") {
            throw new Error(data.message);
        }

        const metrics = data.metrics;

        updateDashboard(metrics);
        updateTable(metrics);
        updateActivity(metrics);

    } catch (error) {

        console.error("Backend error:", error);

        document.getElementById("serverTable").innerHTML = `
            <tr>
                <td colspan="6" class="loading">
                    Unable to connect to backend
                </td>
            </tr>
        `;
    }
}


// Update statistics
function updateDashboard(metrics) {

    if (metrics.length === 0) {
        document.getElementById("totalServers").textContent = "0";
        document.getElementById("avgCpu").textContent = "0%";
        document.getElementById("avgRam").textContent = "0%";
        document.getElementById("anomalies").textContent = "0";
        return;
    }


    // Unique machines
    const machines = [...new Set(
        metrics.map(item => item.machine)
    )];

    document.getElementById("totalServers").textContent =
        machines.length;


    // Average CPU
    const avgCpu =
        metrics.reduce((sum, item) =>
            sum + Number(item.cpu), 0
        ) / metrics.length;


    // Average RAM
    const avgRam =
        metrics.reduce((sum, item) =>
            sum + Number(item.ram), 0
        ) / metrics.length;


    document.getElementById("avgCpu").textContent =
        avgCpu.toFixed(1) + "%";

    document.getElementById("avgRam").textContent =
        avgRam.toFixed(1) + "%";


    document.getElementById("cpuBar").style.width =
        Math.min(avgCpu, 100) + "%";

    document.getElementById("ramBar").style.width =
        Math.min(avgRam, 100) + "%";


    // AI anomaly count
    const anomalies = metrics.filter(
        item => item.prediction === "ANOMALY"
    ).length;

    document.getElementById("anomalies").textContent =
        anomalies;
}


// Server table
function updateTable(metrics) {

    const table = document.getElementById("serverTable");

    if (metrics.length === 0) {

        table.innerHTML = `
            <tr>
                <td colspan="6" class="loading">
                    No monitoring data available
                </td>
            </tr>
        `;

        return;
    }


    // Latest record for each machine
    const latest = {};

    metrics.forEach(item => {

        if (!latest[item.machine]) {
            latest[item.machine] = item;
        }

    });


    table.innerHTML = "";


    Object.values(latest).forEach(item => {

        const prediction =
            item.prediction || "NORMAL";


        const statusClass =
            prediction === "ANOMALY"
                ? "status-anomaly"
                : "status-normal";


        const statusText =
            prediction === "ANOMALY"
                ? "🔴 ANOMALY"
                : "🟢 NORMAL";


        const row = document.createElement("tr");


        row.innerHTML = `
            <td>
                <span class="server-name">
                    ${item.machine}
                </span>
            </td>

            <td>${Number(item.cpu).toFixed(1)}%</td>

            <td>${Number(item.ram).toFixed(1)}%</td>

            <td>${Number(item.disk).toFixed(1)}%</td>

            <td>
                <span class="${statusClass}">
                    ${statusText}
                </span>
            </td>

            <td>
                ${item.timestamp}
            </td>
        `;


        table.appendChild(row);

    });
}


// Recent activity
function updateActivity(metrics) {

    const activity =
        document.getElementById("activity");


    if (metrics.length === 0) {

        activity.innerHTML =
            "<p>No activity available.</p>";

        return;
    }


    activity.innerHTML = "";


    metrics.slice(0, 8).forEach(item => {

        const prediction =
            item.prediction || "NORMAL";


        const status =
            prediction === "ANOMALY"
                ? "🔴 Anomaly detected"
                : "🟢 Server operating normally";


        const div =
            document.createElement("div");


        div.className = "activity-item";


        div.innerHTML = `
            <div>
                <div class="activity-server">
                    ${item.machine}
                </div>

                <div>
                    ${status}
                </div>
            </div>

            <div class="activity-time">
                ${item.timestamp}
            </div>
        `;


        activity.appendChild(div);

    });
}


// Initial load
loadMetrics();


// Auto refresh every 5 seconds
setInterval(loadMetrics, 5000);