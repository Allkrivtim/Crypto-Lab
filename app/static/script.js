document.addEventListener('DOMContentLoaded', function () {
	const content = document.getElementById('content')
	const counter = document.getElementById('counter')
	const clickButton = document.getElementById('clickButton')
	const navButtons = document.querySelectorAll('nav button')

	let tokens = parseInt(localStorage.getItem('tokens') || '0')
	if (counter) {
		counter.textContent = tokens
	}

	console.log('Page loaded, tokens:', tokens)

	if (clickButton) {
		clickButton.addEventListener('click', function () {
			tokens += 1
			counter.textContent = tokens
			localStorage.setItem('tokens', tokens)
			console.log('Button clicked, tokens:', tokens)
			animateClickButton()
		})
	}

	navButtons.forEach(button => {
		button.addEventListener('click', () => {
			const userId = new URLSearchParams(window.location.search).get('user_id')
			console.log(
				'Navigating to:',
				button.getAttribute('data-url'),
				'with user_id:',
				userId
			)
			if (userId) {
				navigateTo(`${button.getAttribute('data-url')}?user_id=${userId}`)
			} else {
				alert('Telegram ID not found')
			}
		})
	})

	function animateClickButton() {
		clickButton.style.animation = 'button-click 0.3s'
		clickButton.addEventListener('animationend', () => {
			clickButton.style.animation = ''
		})
	}

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
		navButtons.forEach(button => fadeOut(button))
		setTimeout(() => {
			window.location.href = url
		}, 500)
	}

	window.addEventListener('load', () => {
		fadeIn(content)
		navButtons.forEach(button => fadeIn(button))
		console.log('Page fully loaded')
	})
})
