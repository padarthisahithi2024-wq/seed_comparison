
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("compareForm");

    if (!form) return;

    const checkboxes = form.querySelectorAll(
        'input[name="seed_ids"]'
    );

    const count = document.getElementById("selectionCount");

    function updateCount() {
        const selected = form.querySelectorAll(
            'input[name="seed_ids"]:checked'
        ).length;

        count.textContent = selected + " seeds selected";
    }

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", updateCount);
    });

    form.addEventListener("submit", function (event) {
        const selected = form.querySelectorAll(
            'input[name="seed_ids"]:checked'
        ).length;

        if (selected < 2) {
            event.preventDefault();
            alert("Please select at least two seeds to compare.");
        }
    });

    updateCount();
});
