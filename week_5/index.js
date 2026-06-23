function calculateGrade() {
    const name = document.getElementById("name").value.trim();
    const score = parseFloat(document.getElementById("scoreInput").value);

    const outName = document.getElementById("outName");
    const outScore = document.getElementById("outScore");
    const outGrade = document.getElementById("outGrade");
    const error = document.getElementById("error");

    // clear previous error
    error.textContent = "";

    // Validation
    if (name === "") {
        error.textContent = "Please enter student name!";
        return;
    }

    if (isNaN(score)) {
        error.textContent = "Please enter a valid score!";
        return;
    }

    if (score < 0 || score > 100) {
        error.textContent = "Score must be between 0 and 100!";
        return;
    }

    // Grade calculation
    let grade;
    if (score >= 70) grade = "A";
    else if (score >= 60) grade = "B";
    else if (score >= 50) grade = "C";
    else if (score >= 40) grade = "D";
    else grade = "F";

    // Display results
    outName.textContent = name;
    outScore.textContent = score;
    outGrade.textContent = grade;

    // disable button briefly (optional "instant feedback feel")
    const btn = document.getElementById("calcBtn");
    btn.textContent = "Calculated ✔";
    btn.disabled = true;

    setTimeout(() => {
        btn.textContent = "Calculate Grade";
        btn.disabled = false;
    }, 1000);
}

function resetForm() {
    document.getElementById("name").value = "";
    document.getElementById("scoreInput").value = "";

    document.getElementById("outName").textContent = "-";
    document.getElementById("outScore").textContent = "-";
    document.getElementById("outGrade").textContent = "-";

    document.getElementById("error").textContent = "";
}