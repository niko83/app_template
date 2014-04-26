DROP TABLE IF EXISTS migrations;
CREATE TABLE IF NOT EXISTS migrations (
    id smallserial,
    key char(32),
    created_at timestamp without time zone default now()
);
insert into migrations (key) values ('s');

select @is_execited:=1 from migrations where key='s';
