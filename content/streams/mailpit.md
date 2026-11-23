+++
title = "mailpit"
date = 2026-11-22
genres = ["stream"]
draft = false
+++

I spent this weekend creating a really pleasant dev experience for email notifications. It's slow and annoying to preview email templates during development by simply sending them to your personal email. So I setup a local SMTP server called Mailpit. I also don't want to point to the local server manually during local dev every time I want to re-route emails for preview, so I configure the Makefile to startup and teardown Mailpit locally. Finally, I decided it would be nice to have an option to configure local testing to either redirect into Mailpit (or use `django.core.mail.backends.locmem.EmailBackend` to drop them in a black hole), so I added a variable that can be configured on the local machine for this behaviorl. This has the added bonus of defaulting to `locmem.EmailBackend` during CI, so that tests pass in the cloud even when no SMTP server is running.
