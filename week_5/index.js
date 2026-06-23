function calculateGrade() {
    const name = document.getElementById("name").value.trim();
    const score = parseFloat(document.getElementById("scoreInput").value);

    const StuName = document.getElementById("StuName");
    const StuScore = document.getElementById("StuScore");
    const StuGrade = document.getElementById("StuGrade");
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
    if (score >= 70) grade = "A (Excellent)";
    else if (score >= 60) grade = "B (Pass)";
    else if (score >= 50) grade = "C (Average)";
    else if (score >= 40) grade = "D (Below Average)";
    else grade = "F (Fail)";

    // Display results
    StuName.textContent = name;
    StuScore.textContent = score;
    StuGrade.textContent = grade;

    // disable button briefly (optional "instant feedback feel")
    const btn = document.getElementById("calcBtn");
    btn.textContent = "Calculated";
    btn.disabled = true;

    setTimeout(() => {
        btn.textContent = "Calculate Grade";
        btn.disabled = false;
    }, 1000);
}

function resetForm() {
    document.getElementById("name").value = "";
    document.getElementById("scoreInput").value = "";

    document.getElementById("StuName").textContent = "-";
    document.getElementById("StuScore").textContent = "-";
    document.getElementById("StuGrade").textContent = "-";

    document.getElementById("error").textContent = "";
}