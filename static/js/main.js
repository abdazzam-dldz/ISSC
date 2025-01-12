const sidebar = document.querySelector(".sidebar");
const linkItems = document.querySelectorAll(".link-item");
const darkMode = document.querySelector(".dark-mode");
const logo = document.querySelector(".logo svg");

//sidebar Hover
sidebar.addEventListener("mouseenter", () => {
  sidebar.classList.add("active");
});

//sidebar Hover Leave
sidebar.addEventListener("mouseleave", () => {
  sidebar.classList.remove("active");
});

//Link-items Clicked
for (let i = 0; i < linkItems.length; i++) {
  if (!linkItems[i].classList.contains("dark-mode")) {
    linkItems[i].addEventListener("click", (e) => {
      linkItems.forEach((linkItem) => {
        linkItem.classList.remove("active");
      });
      linkItems[i].classList.add("active");
    });
  }
}

// Dark Mode Functionality
darkMode.addEventListener("click", function () {
  if (document.body.classList.contains("dark-mode")) {
    // darkMode.querySelector("span").textContent = "dark mode";
    darkMode.querySelector("ion-icon").setAttribute("name", "moon-outline");

    logo.style.fill = "#363b46";
  } else {
    // darkMode.querySelector("span").textContent = "light mode";
    darkMode.querySelector("ion-icon").setAttribute("name", "sunny-outline");
    logo.style.fill = "#fff";
  }
  document.body.classList.toggle("dark-mode");
});


// dropdown-menu
document.addEventListener("DOMContentLoaded", function () {
  const profilePic = document.getElementById("profile-pic");
  const dropdownMenu = document.getElementById("dropdown-menu");

  profilePic.addEventListener("click", function (e) {
    e.preventDefault();
    dropdownMenu.style.display =
      dropdownMenu.style.display === "block" ? "none" : "block";
  });

  // Klik di luar dropdown untuk menutup menu
  window.addEventListener("click", function (e) {
    if (!profilePic.contains(e.target) && !dropdownMenu.contains(e.target)) {
      dropdownMenu.style.display = "none";
    }
  });
});
