const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');

if (menuToggle && nav) {
    menuToggle.addEventListener('click', () => nav.classList.toggle('open'));

    nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => nav.classList.remove('open'));
    });
}
document.querySelectorAll('.product-link').forEach(link => {
  link.addEventListener('click', () => {
    const product = link.dataset.product;
    const select = document.querySelector('select[name="product"]');
    if (select) select.value = product;
  });
});
const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
