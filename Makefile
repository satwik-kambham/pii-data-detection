.PHONY: download_data
download_data:
	kaggle competitions download -c pii-detection-removal-from-educational-data -p ./datasets
	unzip datasets/pii-detection-removal-from-educational-data.zip -d datasets

.PHONY: clean
clean:
	scripts/clean.sh
