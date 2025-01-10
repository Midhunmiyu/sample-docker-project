After all the basic setup, run these following commands
```bash

  docker build -t <any_name>
  docker-compose up --build
```

To get the container ID
```bash

  docker ps -a
```

To get into the docker shell ( run django commands )
```bash

  docker exec -it {container ID} bash
```
