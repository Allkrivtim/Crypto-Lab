document.addEventListener('DOMContentLoaded', async () => {
	const userId = new URLSearchParams(window.location.search).get('user_id')
	if (userId) {
		try {
			const response = await fetch(`/lab?user_id=${userId}`)
			const userData = await response.json()

			// Сохраняем данные пользователя в локальное хранилище
			localStorage.setItem('tokens', userData.tokens)
			localStorage.setItem('mining_speed', userData.mining_speed)
			localStorage.setItem('auto_mining', userData.auto_mining)
			localStorage.setItem('knowledge_points', userData.knowledge_points)
			localStorage.setItem('energy', userData.energy)
			localStorage.setItem(
				'energy_recovery_speed',
				userData.energy_recovery_speed
			)

			// Обновляем отображение данных на странице
			document.getElementById('tokens').innerText = userData.tokens
			document.getElementById(
				'mining_speed'
			).innerText = `x${userData.mining_speed}`
			document.getElementById('auto_mining').innerText = userData.auto_mining
			document.getElementById('knowledge_points').innerText =
				userData.knowledge_points
			document.getElementById('energy').innerText = userData.energy
			document.getElementById('energy_recovery_speed').innerText =
				userData.energy_recovery_speed
		} catch (error) {
			console.error('Error fetching user data:', error)
		}
	}
})

window.addEventListener('beforeunload', async () => {
	const userId = new URLSearchParams(window.location.search).get('user_id')
	if (userId) {
		const userData = {
			tokens: parseInt(localStorage.getItem('tokens')),
			mining_speed: parseInt(localStorage.getItem('mining_speed')),
			auto_mining: parseInt(localStorage.getItem('auto_mining')),
			knowledge_points: parseInt(localStorage.getItem('knowledge_points')),
			energy: parseInt(localStorage.getItem('energy')),
			energy_recovery_speed: parseInt(
				localStorage.getItem('energy_recovery_speed')
			),
		}

		try {
			await fetch(`/lab/update?user_id=${userId}`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(userData),
			})
		} catch (error) {
			console.error('Error updating user data:', error)
		}
	}
})
