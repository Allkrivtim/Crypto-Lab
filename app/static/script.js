document.addEventListener('DOMContentLoaded', async function () {
	const counterDisplay = document.getElementById('counter')
	const clickButton = document.getElementById('clickButton')

	const urlParams = new URLSearchParams(window.location.search)
	const userId = urlParams.get('user_id')

	let counter = parseInt(localStorage.getItem(`tokens_${userId}`)) || 0
	counterDisplay.textContent = counter

	clickButton.addEventListener('click', function () {
		counter++
		counterDisplay.textContent = counter
		localStorage.setItem(`tokens_${userId}`, counter)
	})

	window.addEventListener('beforeunload', async function () {
		await fetch('/update_tokens', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ user_id: userId, tokens: counter }),
		})
	})
})
