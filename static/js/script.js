const searchBox = document.getElementById("searchSymptoms");
const symptomList = document.getElementById("symptomList");

const selectedSymptoms = document.getElementById("selectedSymptoms");
const selectedCount = document.getElementById("selectedCount");

if (searchBox && symptomList) {

    // Search functionality
    searchBox.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        Array.from(symptomList.options).forEach(option => {

            option.style.display =
                option.text.toLowerCase().includes(filter)
                    ? ""
                    : "none";

        });

    });

    // Update selected symptoms list
    symptomList.addEventListener("change", function () {

        selectedSymptoms.innerHTML = "";

        const selected = Array.from(symptomList.selectedOptions);

        selectedCount.textContent = selected.length;

        selected.forEach(option => {

            const li = document.createElement("li");

            li.className = "list-group-item";

            li.innerHTML = `
                <i class="bi bi-check-circle-fill text-success"></i>
                ${option.text}
            `;

            selectedSymptoms.appendChild(li);

        });

    });

}

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

            if (patientName.includes(filter)) {

                row.style.display = "";

            } else {

                row.style.display = "none";

            }

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