# DB MariaDB with docker
All commands are valid in the directory dbmoviemaria

## start docker composition
```
docker compose up -d
docker compose ps
docker compose ps -a
docker volume ls
```

## remove composition
```
docker compose up -d
docker compose down
docker volume rm  maria-dbmovie-data
```

## logs
```
docker compose logs db
```

## shell
```
docker compose exec -it db bash
```

