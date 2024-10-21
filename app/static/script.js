const button = document.getElementById("mine_button");
const scoreElement = document.getElementById("score");

let clicks = 0;
let wait = 0;
let time = 0;
let total_clicks = 0;
let id = 0;
let telegram_id = 0;
let upgrades = 0;
let updatetime = new Date();
let energy = 0;

button.addEventListener("click", function (event) {
  clicks++;
  total_clicks++;
  scoreElement.textContent = total_clicks;
  createParticles(event.clientX, event.clientY); // Создаём частицы
  wait = 1;
  setTimeout(() => {
    wait = 0;
    if (clicks > 0) {
      send_tokens();
    }
  }, 5000);
});

function createParticles(x, y) {
  const particleCount = 10; // Количество частиц при каждом клике
  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement("div");
    particle.classList.add("particle");

    // Случайное смещение частиц от точки клика
    const offsetX = (Math.random() - 0.5) * 100; // Смещение по горизонтали
    const offsetY = (Math.random() - 0.5) * 100; // Смещение по вертикали

    particle.style.left = `${x + offsetX}px`; // Позиционируем частицу
    particle.style.top = `${y + offsetY}px`;

    document.body.appendChild(particle);

    // Удаляем частицу после завершения анимации (2s)
    setTimeout(() => {
      particle.remove();
    }, 2000);
  }
}

function send_tokens() {
  fetch('http://127.0.0.1:8000/api/clicker/tap', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      telegram_id: telegram_id,
      user_id: id,
      user_count: clicks,
      user_time: new Date().toISOString(), // Преобразуем текущее время в строку ISO
      user_updatetime: new Date().toISOString(), // Преобразуем текущее время в строку ISO
      user_upgrades: upgrades,
      user_energy: energy
    })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Ошибка: ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => console.log(data))
    .catch(error => alert(error));
  clicks = 0;
}
