.PHONY: build
build: # Build python venv with deps
	scripts/build.sh

.PHONY: clean
clean: # Cleanup venv build
	scripts/cleanup.sh

.PHONY: txt
txt: # Run main script
	echo "txt" | scripts/run.py

.PHONY: img
img: # Run main script
	echo "img" | scripts/run.py

.PHONY: test
test: # Run main script
	scripts/test.sh

