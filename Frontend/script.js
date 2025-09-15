window.onload = () => {
  const fileInput = document.getElementById("imageUpload");
  const form = document.getElementById("uploadForm");
  const predictionBox = document.getElementById("predictions");
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = fileInput.files[0];
    if (!file) {
      predictionBox.innerText = "Please choose an image.";
      return;
    }
    const img = await createImageBitmap(file);
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);

    const formData = new FormData();
    formData.append("file", file);

    predictionBox.innerText = "Waiting for prediction...";

    try{
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      predictionBox.innerHTML = `
         Predicted: <strong>${data.class}</strong><br>
         Confidence: ${Math.round(data.confidence * 100)}%</br>
         <img src="${data.image_url}" style="max-width: 300px; margin-top: 1rem;" />
         `;
    } catch (err) {
      predictionBox.innerText = "Prediction failed.";
      console.error(err);
    }
  })
}
