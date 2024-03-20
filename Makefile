.PHONY: build_container
build_container:
	podman build -t pii_data_detection:latest .

.PHONY: run_container
run_container:
	podman run -it --rm --device nvidia.com/gpu=all -v $(shell pwd):/mnt pii_data_detection:latest

.PHONY: setup
setup:
	mkdir ~/.kaggle
	cp .kaggle/kaggle.json ~/.kaggle
	chmod 600 ~/.kaggle/kaggle.json

.PHONY: download_data
download_data:
	kaggle competitions download -c pii-detection-removal-from-educational-data -p ./datasets
	unzip datasets/pii-detection-removal-from-educational-data.zip -d datasets

.PHONY: clean
clean:
	scripts/clean.sh
