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

	window.addEventListener('load', () => {
		fadeIn(content)
		console.log(
			'Page loaded with user_id:',
			new URLSearchParams(window.location.search).get('user_id')
		)
	})

	clickButton.addEventListener('click', function () {
		tokens += 1
		counter.textContent = tokens
		localStorage.setItem('tokens', tokens)
		console.log('Button clicked, tokens:', tokens)
	})

	const navButtons = document.querySelectorAll('nav button')
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
})
