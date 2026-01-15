window.addEventListener('scroll', function() {
  const divider = document.querySelector('.custom-divider-nav');
  if (window.pageYOffset > 80) {
    divider.classList.add('visible');
  } else {
    divider.classList.remove('visible');
  }
});


// theme switcher
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const icon = themeToggle.querySelector('i');

const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
  body.classList.add('light-theme');
  icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
}

themeToggle.addEventListener('click', () => {
  body.classList.toggle('light-theme');
  
  if (body.classList.contains('light-theme')) {
    icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
    localStorage.setItem('theme', 'light');
  } else {
    icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    localStorage.setItem('theme', 'dark');
  }
});