+++
linkTitle = 'Gross, Stepinski, and Akşimşek - Hypermedia Systems (2023)'
title = 'Gross, Stepinski, and Akşimşek - Hypermedia Systems (2023)'
shortTitle = 'Hypermedia Systems'
date = 2025-08-06T11:07:55-06:00
genres = ["reading", "2025"]
draft = false
+++

I began using `htmx` sometime in 2023, out of frustration with the prevailing attitudes and communities that dominate the modern Javascript world. Web programming is needlessly complicated, and no one in the React world (which is the world of Javascript in 2025) cares about simplifying things. Too many jobs, livelihoods and paychecks are supported by the complexity hell of React.

These are all terrible reasons to pick a web framework. Yet this is the underlying reasoning for most React developers to choose React (and businesses who hire them). We should choose React because then you can hire more React developers. Imagine any other professional making decisions this way. A dentist choosing a tool that makes them more inefficient, so that more dentists are needed. A doctor intentionally writing everything down instead of using Epic to manage case logs, because now their office can hire more doctors to manage all the paperwork. It's a form of stubborn technological fraud at worst, and downright stupid at best.

I am not interested in supporting the React-industrial complex anymore.

I am looking for a technology that doesn't require me to dedicate my full mental load to simply creating a website. I want to do other things with my time, like orchestrate back-end services, develop embedded software, and play with hardware.

My professional web development career started with Javascript and jQuery. The systems we built were fragile, difficult to test, and hard to reason about. I didn't enjoy this type of programming, but didn't know why at the time. I just thought that this is what software development is supposed to be like.

Later, I was introduced to the next level of abstraction - web frameworks like Gatsby (now defunct), and <a href="https://news.ycombinator.com/item?id=44531635#44535359" target="_blank">Next.js</a> (hopefully meets a similar fate). These were supposed to solve the afore-mentioned problems, but didn't. In my view, they made everything worse. I found myself wishing for jQuery again, a 20+ year-old technology that is still in use by <a href="https://w3techs.com/technologies/overview/javascript_library">73% of all websites on the Internet</a>. Notice where React, Next.js, and Gatsby sit on the list[^soapbox].

---

*Hypermedia Systems* offered me the tools and thinking patterns needed to achieve a mental reset with regards to web development. To realize that yes, things don't have to be complicated. Code can make sense and be highly declarative. You don't need to import hundreds of broken libraries and spend time debugging code that other people wrote. You can own your whole codebase and reason about the whole thing. You can mix and match technologies based on the problem domain. You can be in full control again of your web development experience.

---

Did you know that all of these things are easy to make yourself, and only require a few lines of code in a shell script?

- A local development environment
- A production-equivalent local environment
- Database Migration scripts
- Generation of static files
- Recompilation of Tailwind classes into `styles.css`

These sound like gargantuan tasks, but they're not. Don't believe me? Here is how I solved all of them in 36 lines of code: 

```make
run:
	make configure
	bash .venv/bin/activate
	uv sync
	python3 manage.py migrate
	python3 manage.py runserver

run-prod:
	python manage.py migrate
	gunicorn core.wsgi

configure:
	ln -f git_hooks/* .git/hooks/
	[ -f ".venv/" ] || python3 -m venv .venv
	touch "tailwind.config.js"
	make collstat

tw:
	touch "tailwind.config.js"
	./tailwindcss -i ./static/css/styles.css -o ./static/css/styles.out.css
	make collstat

collstat:
	python3 manage.py collectstatic --no-input

db-make-migrations:
	python3 manage.py makemigrations

db-migrate:
	python3 manage.py migrate

test:
	make configure
	bash .venv/bin/activate
	uv sync
	python3 manage.py test --shuffle -v 2
```
`manage.py` is a Django-generated script. It's not a <a href="https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/" target="_blank">leaky abstraction</a> - I have never needed to peer under the hood to find out what the commands do. But it's not hard to do so - <a href="https://github.com/django/django/tree/main/django/core/management/commands" target="_blank">here it is</a>.

If you can't do these things on your own as a web developer, what exactly is your skillset? You work for Next.js and React, and are an unpaid shill of their ecosystems, because all the features defined above are major selling points of the "great developer experience" they are selling you. They hire the best developer relations folks out there, but YOU, my friend, are their best one! Because you use their product, evangelize it for them on behalf of your company, fix their bugs, and keep using it, despite all the horrible experiences you have had! You sometimes even pay huge amounts of money for the privilege of hosting your website on their platform! You are suffering from Stockholm Syndrome, and know of no way out.

You are a frameworker, not an engineer[^frameworker]. You are forgetting how to code, and instead learning how to use brittle, leaky abstractions that won't hold up over time or end up being transferable skills, as far as being an engineer is concerned.

It doesn't have to be this way. Read Hypermedia Systems. I was able to successfully develop and deploy a medium-sized codebase (10k LoC of Django with HTMX, Alpine.js and Tailwind sprinkled throughout) based on these principles. The code is solving a <a href="https://www.mousehouse.bio" target="_blank">real-world need</a> for scientists at the top university in the country. HTMX isn't a toy or novelty, it gets the job done and lets me focus on the actual real-world problems I want to solve. 

---

> **Hypermedia Control**: A hypermedia control is an element in a hypermedia that describes (or controls) some sort of interaction, often with a remote server, by encoding information about that interaction directly and completely within itself. (page 20)

(More quotes coming)

[^soapbox]: How is it possible that 5% of websites use React, yet seemingly 75% of all web developer job postings ask for React experience? Why does no one ask for jQuery experience, when 73% of websites use it? Simple answer: React code is constantly broken, and needs to be fixed. jQuery codebases are deployed, functional, and solve real problems that people have. You don't hire people to fix things that work.

[^frameworker]: https://archive.ph/XSPRr
