# Полная поэтапная инструкция для Cyberbang Maximal

## Шаг 1. Подготовка и загрузка репозитория
1. Распакуй архив `cyberbang_maximal.zip` локально на ПК или в Replit.
2. Проверь структуру директорий (см. README.md).
3. Создай репозиторий на GitHub: `cyberbang`.
4. Загрузите все файлы через GitHub UI или локальным Git:
   ```bash
   cd cyberbang_maximal
   git init
   git remote add origin https://github.com/ВАШ_ЛОГИН/cyberbang.git
   git add .
   git commit -m "Initial Cyberbang Maximal"
   git push -u origin main
   ```

## Шаг 2. Настройка среды разработки (Replit / локально)
### Вариант Replit (рекомендуется для Windows 7)
1. Импортируй репозиторий в Replit.
2. В Replit установятся Node.js и Python по `replit.nix` автоматически.
3. В разделе Secrets добавь переменные из `.env.example`, заполнив известные: BOT_TOKEN, SUPABASE_URL, SUPABASE_KEY, TON_WALLET, OPENAI_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID, SENTRY_DSN, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BACKEND_URL (пока placeholder).
4. Нажми "Run" — запустится `start.sh`: сборка frontend, backend, бот.

### Локальный запуск через Docker Compose
1. Установи Docker и Docker Compose.
2. Перейди в каталог с распакованными файлами.
3. Заполни `.env` на основе `.env.example`.
4. Запусти:
   ```bash
   docker-compose up --build
   ```
5. Сервисы:
   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000
   - Telegram-бот локально при использовании webhook (нужно дополнить)

## Шаг 3. Настройка инфраструктуры (AWS + Terraform)
1. Конфигурация Terraform в `infra/terraform/` (пути ниже). Проверить файлы в infra.
2. В `.env` задать AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION.
3. Запусти:
   ```bash
   cd infra/terraform
   terraform init
   terraform apply
   ```
   Это создаст VPC, EC2 или ECS кластер, RDS для базы, S3 для статики, Load Balancer.
4. Деплой backend контейнера в ECS, frontend статика в S3+CloudFront или Vercel. 
5. После деплоя обнови BACKEND_URL и NEXT_PUBLIC_BACKEND_URL в Secrets GitHub/Vercel.

## Шаг 4. CI/CD с GitHub Actions
1. В `.github/workflows/` есть рабочие файлы для frontend, backend, asset generation.
2. Настрой Secrets GitHub: VERCEL_TOKEN, AWS credentials, SUPABASE keys, etc.
3. При пуше в main:
   - Frontend собирается и деплоится на Vercel или S3.
   - Backend собирается в Docker и деплоится на ECS через GitHub Actions.
   - Asset Generation workflow запускает генерацию артов и сохраняет результаты в S3/IPFS.
4. Notion integration вызывает обновление статусов при деплое.

## Шаг 5. Интеграция TON смарт-контрактов
1. Локально или в CI:
   - Установи `@ton-community/assets-cli` для deploy Jetton и NFT.
   - Загрузи иконки в IPFS (скрипт `scripts/upload_to_ipfs.py`).
   - Выполни deploy командой:
     ```bash
     assets-cli deploy-jetton --name "Cyberbang Token" --symbol "CBG" --icon <IPFS_URL>
     assets-cli deploy-nft-collection --collection-name "Cyberbang Heroes" --metadata <IPFS metadata>
     ```
   - Сохрани адреса контрактов.
2. В backend добавить модули для взаимодействия с TON SDK (пример: `backend/ton_client.py`).
3. Автоматизировать: CI-сценарий при релизе вызывает deploy контрактов на testnet через секреты CLI ключа.

## Шаг 6. Supabase и база данных
1. Таблицы:
   - users, nfts, quests, transactions, analytics_events.
2. Миграции SQL в `infra/supabase/migrations/` (файлы .sql).
3. Backend использует Supabase Python SDK.
4. Analytics скрипты: `analytics/analyze_metrics.py` подключается к Supabase и строит отчёты (Retent, LTV, Cohorts).
5. CI может выполнять миграции автоматически при пуше.

## Шаг 7. AI-модули
1. **Asset Generation**: `ai_asset_generation/generate_assets.py` генерирует арты через OpenAI или Stable Diffusion. CI сохраняет в S3/IPFS.
2. **Quest & Content Generation**: `ai_modules/generate_quests.py` генерирует описания квестов и параметры сложности через LLM.
3. **Chat Assistant**: `frontend/pages/chat.tsx` и backend `/api/chat` для поддержки игроков.
4. **Analytics Assistant**: `analytics/ai_insights.py` подключает к OpenAI, отправляет сводку метрик и получает рекомендации по улучшению.
5. **Marketing Automation**: скрипты `marketing/generate_campaigns.py` генерируют тексты для соцсетей, e-mail рассылок.
6. **Code Review & Security**: GitHub Actions интеграция с LLM для автоматического ревью PR (placeholder scripts).
7. **DevOps Automation**: `infra/auto_scale.py` использует ML для прогнозирования нагрузки и масштабирования инфраструктуры.

## Шаг 8. Тестирование и локальная разработка
1. Docker Compose для локальной разработки:
   - `docker-compose.yml` поднимает backend, frontend dev server, Postgres (для эмуляции Supabase), Redis.
2. Тестовые токены TON можно симулировать или подключить testnet через локальный TON SDK.
3. Телеграм-бот локально: использовать ngrok для webhook, или polling.
4. Обязательно покрыть backend тестами: `tests/` с pytest и используют fixtures Supabase эмулятора.

## Шаг 9. Мониторинг и логирование
1. Интеграция Sentry в backend (Python) и frontend (JS) для отслеживания ошибок.
2. CloudWatch (AWS) или альтернативы для логов инфраструктуры.
3. Analytics в Supabase, дашборд в Metabase/Redash (scripts добавлены).
4. AI-анализ логов: `monitoring/ai_log_insights.py` ищет аномалии.

## Шаг 10. Публичный запуск
1. Убедиться, что контракты протестированы и задеплоены на mainnet.
2. Обновить переменные окружения (RPC mainnet).
3. Запустить продакшн-инстансы (ECS/Vercel).
4. Настроить CI/CD для mainnet релизов.
5. Выполнить маркетинговые кампании, airdrop.
6. Continuously monitor метрики и фитбек.

## Шаг 11. Дальнейшее развитие
- DAO-модуль: `backend/dao.py` для голосований.
- Cross-chain bridge: скрипты и интеграции.
- Мобильные приложения: PWA оболочка или React Native wrapper.
- Сообщество: инструменты UGC, создание пользовательских квестов.
- Экономические модели: `analytics/economics_simulation.py` с симуляциями токеномики.
