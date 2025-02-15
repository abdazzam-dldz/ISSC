const container = document.querySelector(".sidebar");
const linkItems = document.querySelectorAll(".link-item");
const headerItems = document.querySelectorAll(".header-item");
const darkMode = document.querySelector(".dark-mode a"); // Pilih link dalam .dark-mode
const logo = document.querySelector(".logo svg");
const pageName = document.querySelector("#page-name"); // Pilih elemen page-name

// Container Hover
container.addEventListener("mouseenter", () => {
  container.classList.add("active");
  pageName.style.marginLeft = "260px"; // Ubah margin-left saat sidebar aktif
});

// Container Hover Leave
container.addEventListener("mouseleave", () => {
  container.classList.remove("active");
  pageName.style.marginLeft = "85px"; // Kembalikan margin-left saat sidebar tidak aktif
});

// // Link-items Clicked
// for (let i = 0; i < linkItems.length; i++) {
//   if (!linkItems[i].classList.contains("dark-mode")) {
//     linkItems[i].addEventListener("click", (e) => {
//       linkItems.forEach((linkItem) => {
//         linkItem.classList.remove("active");
//       });
//       linkItems[i].classList.add("active");
//     });
//   }
// }

// Dark Mode Functionality
darkMode.addEventListener("click", function (e) {
  e.preventDefault(); // Mencegah reload halaman saat klik link

  document.body.classList.toggle("dark-mode");

  // Ubah ikon mode gelap/terang
  const icon = darkMode.querySelector("ion-icon");
  if (document.body.classList.contains("dark-mode")) {
    icon.setAttribute("name", "sunny-outline"); // Ubah ke ikon terang
    logo.style.fill = "#fff"; // Sesuaikan warna logo
  } else {
    icon.setAttribute("name", "moon-outline"); // Ubah ke ikon gelap
    logo.style.fill = "#363b46";
  }
});


document.addEventListener("DOMContentLoaded", function () {
  const profileBtn = document.querySelector(".profile-btn");
  const profileMenu = document.querySelector(".profile");

  profileBtn.addEventListener("click", function (event) {
      event.preventDefault();
      profileMenu.classList.toggle("active");
      console.log("Dropdown toggled:", profileMenu.classList.contains("active")); // Debugging
  });

  document.addEventListener("click", function (event) {
      if (!profileMenu.contains(event.target) && !profileBtn.contains(event.target)) {
          profileMenu.classList.remove("active");
          console.log("Dropdown closed"); // Debugging
      }
  });
});




