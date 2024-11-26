const mockDevicesUrl = "http://127.0.0.1:8000/api/mock-fetch/";
const updateDevicesUrl = "http://127.0.0.1:8000/api/update-devices/";
const allDevicesUrl = "http://127.0.0.1:8000/api/devices/";

// Fetch Mock Devices
async function fetchMockDevices() {
    try {
        const response = await fetch(mockDevicesUrl);
        const data = await response.json();
        renderTable(data);
    } catch (error) {
        alert("Error fetching mock devices: " + error.message);
    }
}

// Fetch and Store Devices
async function updateDevices() {
    try {
        const response = await fetch(updateDevicesUrl);
        const data = await response.json();
        alert(data.message || "Devices successfully updated.");
    } catch (error) {
        alert("Error updating devices: " + error.message);
    }
}

// Get All Devices
async function getAllDevices() {
    try {
        const response = await fetch(allDevicesUrl);
        const data = await response.json();
        renderTable(data);
    } catch (error) {
        alert("Error fetching all devices: " + error.message);
    }
}

// Get Filtered Devices
async function getFilteredDevices(status) {
    try {
        const url = `${allDevicesUrl}?status=${status}`;
        const response = await fetch(url);
        const data = await response.json();
        renderTable(data);
    } catch (error) {
        alert(`Error fetching ${status} devices: ` + error.message);
    }
}

// Render Table
function renderTable(devices) {
    const tableBody = document.getElementById("deviceTableBody");
    tableBody.innerHTML = ""; // Clear the table

    devices.forEach(device => {
        const row = `
      <tr>
        <td>${device.device_id}</td>
        <td>${device.hostname}</td>
        <td>${device.ip_address}</td>
        <td>${device.status}</td>
        <td>${device.location}</td>
      </tr>
    `;
        tableBody.insertAdjacentHTML("beforeend", row);
    });
}