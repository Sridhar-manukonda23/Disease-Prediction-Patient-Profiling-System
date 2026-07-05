// -----------------------------
// Symptoms Search & Selection
// -----------------------------

const searchBox = document.getElementById("searchSymptoms");

const symptomItems = document.querySelectorAll(".symptom-item");

const checkboxes = document.querySelectorAll(".symptom-checkbox");

const selectedSymptoms = document.getElementById("selectedSymptoms");

const selectedCount = document.getElementById("selectedCount");

// Search Symptoms

if (searchBox) {

    searchBox.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        symptomItems.forEach(item => {

            const text = item.innerText.toLowerCase();

            item.style.display = text.includes(filter)
                ? "block"
                : "none";

        });

    });

}

// Update Selected Symptoms

function updateSelectedSymptoms() {

    selectedSymptoms.innerHTML = "";

    let count = 0;

    checkboxes.forEach(box => {

        if (box.checked) {

            count++;

            const li = document.createElement("li");

            li.className = "list-group-item";

            li.innerHTML = `
                <i class="bi bi-check-circle-fill text-success"></i>
                ${box.nextElementSibling.innerText}
            `;

            selectedSymptoms.appendChild(li);

        }

    });

    selectedCount.textContent = count;

}

checkboxes.forEach(box => {

    box.addEventListener("change", updateSelectedSymptoms);

});

// -----------------------------
// Search Patient History
// -----------------------------

const searchPatient = document.getElementById("searchPatient");

if (searchPatient) {

    searchPatient.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        const rows = document.querySelectorAll("#historyTable tbody tr");

        rows.forEach(row => {

            const patientName = row.cells[1].textContent.toLowerCase();

            row.style.display = patientName.includes(filter)
                ? ""
                : "none";

        });

    });

}

// -----------------------------
// AI Loading Button
// -----------------------------

const form = document.querySelector("form");

const predictBtn = document.getElementById("predictBtn");

if (form && predictBtn) {

    form.addEventListener("submit", function () {

        predictBtn.disabled = true;

        predictBtn.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Predicting Disease...
        `;

    });

}
