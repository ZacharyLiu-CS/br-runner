.PHONY: build run

build:
	@if [ ! -d "tikv-venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv tikv-venv; \
	else \
		echo "Virtual environment already exists."; \
	fi
	@echo "Installing requirements..."
	@. tikv-venv/bin/activate && pip3 install -r requirements.txt

run:
	@echo "Running get_hosts.py..."
	@. tikv-venv/bin/activate && python3 get_hosts.py
