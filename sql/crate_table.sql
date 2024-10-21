CREATE TABLE clicker (
    user_id SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    user_count INTEGER NOT NULL,
    user_upgrades INTEGER NOT NULL,
    user_time BIGINT NOT NULL,
    user_updatetime BIGINT NOT NULL,
    user_energy INTEGER NOT NULL
);