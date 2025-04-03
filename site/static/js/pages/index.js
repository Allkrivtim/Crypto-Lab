const button_elm = document.getElementById("mine_button");
const score_elm = document.getElementById("score");
const energy_elm = document.getElementById("energy");
const btn = document.getElementById("btn_1");

let clicks = 0;
let wait = 0;
let time = 0;
let total_clicks = 0;
let id = 0;
let telegram_id = 0;
let upgrades = 0;
let updatetime = new Date();
let energy = 100;
let max_energy = 100;
let regeneration_energy = true;


if (regeneration_energy == true) {
  if (energy < max_energy) {
    energy += 1;
    energy_elm.textContent = energy;
  }
}

button_elm.addEventListener("click", function (event) {
  if (energy > 0) {
    clicks++;
    total_clicks++;
    score_elm.textContent = total_clicks;
    energy_elm.textContent = energy;
    createParticles(event.clientX, event.clientY); // Создаём частицы
    wait = 1;
    setTimeout(() => {
      wait = 0;
      if (clicks > 0) {
        send_tokens();
      }
    }, 5000);
    energy--;
  }
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