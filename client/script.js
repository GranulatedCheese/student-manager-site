// Base Url
const API_URL = "http://127.0.0.1:5000/students";
console.log("SCRIPT LOADED");

function loadStudents() {
  fetch(API_URL)
    .then((res) => res.json())
    .then((data) => {
      const list = document.getElementById("studentList");
      list.innerHTML = "";
      data.forEach((student) => {
        const li = document.createElement("li");
        li.className =
          "list-group-item d-flex justify-content-between align-items-center  student-list";
        li.innerHTML = `
          <span>${student.name} — Grade: ${student.grade}</span>
          <input type="text" class="form-control edit-form" placeholder="Grade" id="editForm${student.id}">
          <button class="btn btn-success btn-sm" onclick="editStudent(${student.id})">Edit</button>
          <button class="btn btn-danger btn-sm" onclick="deleteStudent(${student.id})">Delete</button>
        `;
        list.appendChild(li);
      });
    });
}

// Get Student's Average
const getAverageButton = document.getElementById("getAverage");
getAverageButton.addEventListener("click", (e) => {
  e.preventDefault();

  fetch(`${API_URL}/class-average`, {
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => {
      // data is just an object. the reason i used data.message is because in student_r, the message is prefix with 'message'
      document.getElementById("studentAverage").innerHTML = `${data.message}`;
    });
});

// Edit Student's Grade
function editStudent(id) {
  const grade = document.getElementById(`editForm${id}`).value.trim();

  if (!grade) {
    console.log("No Value Indicated.");
    return;
  }

  fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ grade }),
  })
    .then((res) => res.json())
    .then(() => {
      loadStudents();
      document.getElementById("grade").value = "";
    });
}

// Add a new student
const addFormButton = document.getElementById("addForm");
addFormButton.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value.trim();
  const grade = document.getElementById("grade").value.trim();

  if (!name || !grade) return;

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, grade }),
  })
    .then((res) => res.json())
    .then(() => {
      loadStudents();
      document.getElementById("name").value = "";
      document.getElementById("grade").value = "";
    });
});

// Delete student
function deleteStudent(id) {
  fetch(`${API_URL}/${id}`, {
    method: "DELETE",
  }).then(() => loadStudents());
}

loadStudents();
