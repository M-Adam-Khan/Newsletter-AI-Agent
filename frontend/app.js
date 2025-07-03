const generateBtn = document.getElementById("generateBtn");
const topicInput = document.getElementById("topicInput");
const responseBox = document.getElementById("responseBox");
const downloadLink = document.getElementById("downloadLink");
const loader = document.getElementById("loader");

generateBtn.addEventListener("click", generateNewsletter);

async function generateNewsletter() {
  const topic = topicInput.value.trim();
  if (!topic) {
    alert("Please enter a newsletter topic.");
    return;
  }

  // Reset UI
  responseBox.classList.add("hidden");
  downloadLink.classList.add("hidden");
  loader.classList.remove("hidden");
  generateBtn.disabled = true;
  topicInput.disabled = true;

  try {
    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ topic }),
    });

    if (!response.ok) {
      throw new Error("Failed to generate newsletter. Please try again.");
    }

    const data = await response.json();

    // Show newsletter content
    responseBox.textContent = data.newsletter;
    responseBox.classList.remove("hidden");

    // Show download button
    const encodedFilename = encodeURIComponent(data.filename);
    downloadLink.innerHTML = `<a href="http://127.0.0.1:8000/download/${encodedFilename}" target="_blank" rel="noopener noreferrer"> Download Word Document </a>`;
    downloadLink.classList.remove("hidden");
  } catch (error) {
    responseBox.textContent = `❌ Error: ${error.message}`;
    responseBox.classList.remove("hidden");
  } finally {
    loader.classList.add("hidden");
    generateBtn.disabled = false;
    topicInput.disabled = false;
  }
}
