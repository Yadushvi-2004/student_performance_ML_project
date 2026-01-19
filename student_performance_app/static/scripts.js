function getPrediction() {
    const data = {
        hours: document.getElementById("hours").value,
        previous_score: document.getElementById("previous_score").value,
        sleep: document.getElementById("sleep").value,
        papers: document.getElementById("papers").value,
        activity: document.getElementById("activity").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerHTML =
            "📊 Predicted Performance Index: <b>" + result.prediction + "</b>";
    });
}
