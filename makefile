.PHONY: docker
.PHONY: test
.PHONY: frontendtest
.PHONY: dockerclose

docker:
	docker build -t flask_ex1 .
	docker run -itd -p 9090:9090 --rm -v ${PWD}/app:/src/app --name flask_ex1_con flask_ex1
	docker logs flask_ex1_con -f
dockerclose:
	docker stop flask_ex1_con
test:
	cd app/test && coverage run -m pytest && coverage report -m && coverage html
frontendtest: run1 run2 run3 run4 run5 run6
	@echo "All scripts ran successfully."

run1:
	@echo "Running 1.py"
	@cd frontendtesting && python3 1.py

run2:
	@echo "Running 2.py"
	@cd frontendtesting && python3 2.py

run3:
	@echo "Running 3.py"
	@cd frontendtesting && python3 3.py

run4:
	@echo "Running 4.py"
	@cd frontendtesting && python3 4.py

run5:
	@echo "Running 5.py"
	@cd frontendtesting && python3 5.py

run6:
	@echo "Running 6.py"
	@cd frontendtesting && python3 6.py


