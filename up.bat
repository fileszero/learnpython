setlocal

cd /d %~dp0\docker

docker-compose up -d %*
docker-compose exec python3 bash
echo please execute : docker-compose down
