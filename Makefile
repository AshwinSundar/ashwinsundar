run:
	hugo server run

tw:
	cd themes/ashwin && ./tw-gen.sh

new-post:
	@read -p "Enter the name of the post: " NAME; \
	hugo new "content/posts/$$NAME.md"

new-reading:
	@read -p "Enter the name of the reading: " NAME; \
	hugo new "content/reading/$$NAME.md"
