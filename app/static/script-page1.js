document.addEventListener('DOMContentLoaded', function () {
	const sections = document.querySelectorAll('.section')
	const h1Element = document.querySelector('h1')

	// Запускаем анимацию для каждого раздела и заголовка
	sections.forEach(section => {
		section.style.animation = 'slideIn 0.5s forwards'
		section.style.animationDelay = '0.1s' // Добавляем задержку для плавности анимации
	})

	if (h1Element) {
		h1Element.style.animation = 'slideIn 0.5s forwards'
	}
	const currentPage = window.location.pathname // Получаем текущий URL страницы

	const links = document.querySelectorAll('.footer-button')
	links.forEach(link => {
		// Проверяем, если ссылка соответствует текущему URL, добавляем класс active
		if (link.getAttribute('href') === currentPage) {
			link.classList.add('active')
		}
	})
})
