-- Creates the table with an unique_ID.
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);

