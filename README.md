# flask_ex1
A docker environment for Flask with coding examples

Open a shell and move to the flask_ex1 folder. Under the folder, execute the following commend
```
docker build -t flask_ex1 .
``` 

You should see a image flask_ex1.

```
docker run -itd -p 9090:9090 --rm -v ${PWD}/app:/src/app --name flask_ex1_con flask_ex1
```

You can check the flask server log by using docker container logs command

```
docker logs flask_ex1_con -f
```

For tests

```
pip install pytest
``` 

```
pytest
``` 
