CREATE TABLE IF NOT EXISTS migrations (
    id smallserial,
    key char(32),
    created_at timestamp without time zone default now()
);
