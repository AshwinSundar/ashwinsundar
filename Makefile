run:
	make configure
	.venv/bin/uvicorn app.main:app --reload

run-prod:
	make configure
	.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

configure:
	[ -d .venv ] || python3 -m venv .venv
	uv sync

tw:
	./tailwindcss -c tailwind.config.js -i static/css/tw.css -o static/css/o.tw.css --minify

tw-watch:
	./tailwindcss -c tailwind.config.js -i static/css/tw.css -o static/css/o.tw.css --minify --watch

new-post:
	@read -p "Slug (kebab-case): " SLUG; \
	FILE="content/posts/$$SLUG.md"; \
	[ -f "$$FILE" ] && echo "$$FILE already exists" && exit 1; \
	printf '+++\ntitle = ""\ndate = %s\ngenres = []\ndraft = true\n+++\n' $$(date +%Y-%m-%d) > "$$FILE"; \
	echo "Created $$FILE"

new-reading:
	@read -p "Slug (kebab-case): " SLUG; \
	FILE="content/reading/$$SLUG.md"; \
	[ -f "$$FILE" ] && echo "$$FILE already exists" && exit 1; \
	printf '+++\ntitle = ""\ndate = %s\ngenres = ["reading", "%s"]\ndraft = false\n+++\n' $$(date +%Y-%m-%d) $$(date +%Y) > "$$FILE"; \
	echo "Created $$FILE"
