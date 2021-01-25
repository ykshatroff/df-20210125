# df-20210125

Some Docker and docker-compose examples.

* `docker build -t TAG .` builds a container from the Dockerfile and tags it with TAG.
* `docker run TAG` starts the container tagged  with TAG (without terminal input or output), and runs the default command.
* `docker run -it TAG` runs the container tagged  with TAG with terminal input and output.
* `docker run -it TAG COMMAND` runs the command COMMAND in the container tagged with TAG.
* `docker-compose up -d` creates containers for all services from the `docker-compose.yml` file and starts them, executing the commands as set in the `command` section of each service, or the default command from the container.
* `docker-compose up -d SERVICE` starts a particular service.
* `docker-compose run SERVICE` runs a particular service, creating a new container for it.
* `docker-compose run SERVICE COMMAND` runs COMMAND a particular service, creating a new container for it.
* `docker-compose stop SERVICE` stops a container for the service. Without SERVICE, stops all started containers.
* `docker-compose rm SERVICE` removes a container for the service. Without SERVICE, removes all containers that are not running.
