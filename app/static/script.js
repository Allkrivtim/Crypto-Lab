document.addEventListener('DOMContentLoaded', function () {
	// Анимация вылета элементов страницы, кроме блока кнопок и кнопок
	const elementsToAnimate = document.querySelectorAll('.click-counter, h1')

	elementsToAnimate.forEach(element => {
		element.style.opacity = '0'
		element.style.transform = 'translateY(50px)'
		element.style.animation = 'slideIn 0.5s forwards'
	})

	const mainButton = document.getElementById('mainButton')
	const clickCounter = document.getElementById('clickCounter')
	let count = localStorage.getItem('clickCount') || 0

	if (clickCounter) {
		clickCounter.textContent = count
	}

	if (mainButton) {
		mainButton.addEventListener('click', function () {
			count++
			clickCounter.textContent = count
			localStorage.setItem('clickCount', count)
		})
		// Добавляем анимацию вылета для главной кнопки
		mainButton.style.opacity = '0'
		mainButton.style.transform = 'translateY(50px)'
		mainButton.style.animation = 'slideIn 0.5s forwards'
		mainButton.style.animationDelay = '0.5s' // Добавляем задержку для анимации
	}

	// Добавляем обработчик для открытия и закрытия затемнения
	function toggleOverlay() {
		const overlay = document.querySelector('.overlay')
		if (overlay) {
			// Проверяем, что элемент существует
			overlay.classList.toggle('active')
		}
	}

	links.forEach(link => {
		link.addEventListener('click', function (event) {
			// Предотвращаем переход по ссылке
			event.preventDefault()

			// Задержка перед переходом на новую страницу
			setTimeout(() => {
				window.location.href = link.getAttribute('href')
			}, 500) // Задержка в 0.5 секунды (500 миллисекунд)
		})
	})
	const currentPage = window.location.pathname // Получаем текущий URL страницы

	const links = document.querySelectorAll('.footer-button')
	links.forEach(link => {
		// Проверяем, если ссылка соответствует текущему URL, добавляем класс active
		if (link.getAttribute('href') === currentPage) {
			link.classList.add('active')
		}
	})
})
