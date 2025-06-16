-- Пример миграций Supabase
create table if not exists users (
  address text primary key,
  telegram_id bigint,
  balance numeric default 0,
  created_at timestamp default now()
);
create table if not exists nfts (
  id serial primary key,
  owner text references users(address),
  token_address text,
  metadata jsonb,
  minted_at timestamp default now()
);
create table if not exists quests (
  id serial primary key,
  name text,
  reward numeric,
  description text
);
create table if not exists quest_results (
  id serial primary key,
  user_address text references users(address),
  quest_id int references quests(id),
  result text,
  reward numeric,
  completed_at timestamp default now()
);
