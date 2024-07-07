async function syncWithDatabase(user_id, tokens) {
	console.log(
		'Starting sync with database for user_id:',
		user_id,
		'tokens:',
		tokens
	)

	const data = {
		user_id: user_id,
		tokens: tokens,
		mining_speed: 1,
		auto_mining: 0,
		knowledge_points: 0,
		energy: 100,
		energy_recovery_speed: 1,
	}

	try {
		const response = await fetch('/api/sync', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})

		if (response.ok) {
			const result = await response.json()
			console.log('Sync successful:', result)
		} else {
			console.error('Sync failed with status:', response.status)
		}
	} catch (error) {
		console.error('Error syncing with database:', error)
	}
}
