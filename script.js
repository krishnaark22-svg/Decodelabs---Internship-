async function checkPassword() {
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password: password })
    });

    const data = await response.json();
    document.getElementById("result").innerText = "Strength: " + data.strength;
}
