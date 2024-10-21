CREATE SCHEMA IF NOT EXISTS content;

-- Подключение расширения для генерации UUID версии 4 (UUID4)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE content.clicker (
    id uuid PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    user_count INTEGER NOT NULL,
    user_upgrades INTEGER NOT NULL,
    user_time BIGINT NOT NULL,
    user_updatetime BIGINT NOT NULL,
    user_energy INTEGER NOT NULL
);

-- Пример записи данных с автоматической генерацией UUID4
INSERT INTO content.clicker (id, telegram_id, user_count, user_upgrades, user_time, user_updatetime, user_energy)
VALUES (uuid_generate_v4(),
        9223372036,
        1,
        1,
        9223372036,
        9223372036,
        100);
