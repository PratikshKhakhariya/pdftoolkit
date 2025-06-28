document.addEventListener("DOMContentLoaded", () => {
  const uploadArea = document.getElementById("uploadArea");
  const fileInput = document.getElementById("fileInput");
  const fileList = document.getElementById("fileList");
  const form = document.getElementById("mergeForm");
  const loader = document.getElementById("loader");

  uploadArea.addEventListener("click", () => fileInput.click());

  uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.classList.add("highlight");
  });

  uploadArea.addEventListener("dragleave", () => {
    uploadArea.classList.remove("highlight");
  });

  uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;
    showFiles(fileInput.files);
  });

  fileInput.addEventListener("change", () => {
    showFiles(fileInput.files);
  });

  form.addEventListener("submit", () => {
    loader.style.display = "block";
  });

  function showFiles(files) {
    fileList.innerHTML = "";
    Array.from(files).forEach(file => {
      const div = document.createElement("div");
      div.textContent = "📄 " + file.name;
      fileList.appendChild(div);
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const darkSwitch = document.getElementById("darkModeSwitch");

  // Load saved mode
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    darkSwitch.checked = true;
  }

  // Toggle dark mode
  darkSwitch.addEventListener("change", () => {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
  });
});
