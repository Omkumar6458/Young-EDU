
function toggleSubtopics(topicId) {
  const subtopics = document.getElementById(topicId);
  if (subtopics.style.display === "none" || subtopics.style.display === "") {
      subtopics.style.display = "block";
  } else {
      subtopics.style.display = "none";
  }
}

function loadContent(file) {
  const contentDiv = document.getElementById("content");
  contentDiv.innerHTML = `<iframe src="${file}" style="width: 100%; height: 100%; border: none;"></iframe>`;
  
}

function toggleMenu() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('hidden');
  sidebar.classList.toggle('open');
}

