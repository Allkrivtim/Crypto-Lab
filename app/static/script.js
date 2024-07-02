document.addEventListener('DOMContentLoaded', function () {
	const content = document.getElementById('content')
	const counter = document.getElementById('counter')
	const clickButton = document.getElementById('clickButton')

	let tokens = parseInt(localStorage.getItem('tokens') || '0')
	counter.textContent = tokens

	function fadeOut(element) {
		element.style.transition = 'opacity 0.5s ease-out'
		element.style.opacity = 0
	}

	function fadeIn(element) {
		element.style.transition = 'opacity 0.5s ease-in'
		element.style.opacity = 1
	}

	function navigateTo(url) {
		fadeOut(content)
		setTimeout(() => {
			window.location.href = url
		}, 500)
	}

	window.addEventListener('load', () => fadeIn(content))

	clickButton.addEventListener('click', function () {
		tokens += 1
		counter.textContent = tokens
		localStorage.setItem('tokens', tokens)
	})

	const navButtons = document.querySelectorAll('nav button')
	navButtons.forEach(button => {
		button.addEventListener('click', () => {
			navigateTo(button.getAttribute('data-url'))
		})
	})
})
