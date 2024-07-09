document.addEventListener('DOMContentLoaded', function () {
	const mainButton = document.getElementById('mainButton')
	const clickCounter = document.getElementById('clickCounter')

	// Проверяем, есть ли уже сохраненное значение в Local Storage
	let count = localStorage.getItem('clickCount') || 0
	clickCounter.textContent = `Нажатий: ${count}`

	mainButton.addEventListener('click', function () {
		count++
		clickCounter.textContent = `Нажатий: ${count}`
		localStorage.setItem('clickCount', count)
	})

	// Добавляем активный индикатор над текущей страницей в футере
	const buttons = document.querySelectorAll('.footer-button')
	buttons.forEach((button, index) => {
		button.addEventListener('click', function () {
			// Удаляем активный класс у всех кнопок
			buttons.forEach(btn => btn.classList.remove('active'))
			// Добавляем активный класс к текущей кнопке
			button.classList.add('active')

			// Позиционируем полоску над текущей кнопкой
			const indicator = document.querySelector('.active-indicator')
			indicator.style.width = `${button.offsetWidth}px`
			indicator.style.transform = `translateX(${button.offsetLeft}px)`
		})
	})
})
