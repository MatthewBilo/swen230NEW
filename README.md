# SWEN 230 Final Project
A simple website and testing

Open a shell and move to the SWEN230 folder. Under the folder, execute the following commend
```
make docker
``` 

You can check the flask server log by using docker container logs command

```
docker logs flask_ex1_con -f
```
## Testing

For our testing we unit tested all the commands and all their possible outputs. We are currently expecting all the correct outputs based on the certain input. We are currently achieving all the correct outputs also. 
For unit tests you should execpt 16 tests that are all passing with 100% coverage. For front end testing, with docker freshly started with no previous attempts at front end testing, should pass all 7 front end tests. 
The units test report is printed out in the console and also put in an html file in the ./test/htmlcov folder, the file name is index.html. All the front end test results are printed out in the console. 

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
