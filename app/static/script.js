const button = document.getElementById('mine_button');

let clicks = 0;
let wait = 0;
let time = 0;
let total_clicks = 0;
let id = 0;
let telegram_id = 0;
let upgrades = 0;
let updatetime = 0;
let energy = 0;



button.addEventListener('click', function () {
  clicks++;
  total_clicks++;
  if (wait === 1) {
    return;
  }

  wait = 1;
  setTimeout(() => {
    wait = 0;
    if (clicks > 0) {
      send_tokens();
    }
  }, 5000);
});

function send_tokens() {
  fetch('http://127.0.0.1:8000/api/clicker/tap', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      telegram_id: telegram_id,
      user_id: id,
      user_count: clicks,
      user_time: time,
      user_updatetime: updatetime,
      user_upgrades: upgrades,
      user_energy: energy
    })
  })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => alert(error));
}
