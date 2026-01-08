window.addEventListener('scroll', function() {
  const divider = document.querySelector('.custom-divider-nav');
  if (window.pageYOffset > 80) {
    divider.classList.add('visible');
  } else {
    divider.classList.remove('visible');
  }
});