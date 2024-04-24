# flask_ex1
A docker environment for Flask with coding examples

Open a shell and move to the flask_ex1 folder. Under the folder, execute the following commend
```
make docker
``` 

You can check the flask server log by using docker container logs command

```
docker logs flask_ex1_con -f
```

For unit tests

```
pip install pytest
``` 

```
make test
``` 

For frontend tests (Note, if you want to run front end test multiple times, you need to restart the container, run 'make dockerclose' then 'make docker' to restart the container)

```
make frontendtest
```
