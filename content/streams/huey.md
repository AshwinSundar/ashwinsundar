+++
title = "Huey"
date = 2026-11-04
genres = ["stream"]
draft = false
+++

Last couple days have been very productive! MouseHouse has two new superpowers - an email backend, and a task queue. The task queue, `huey`, is exciting. MouseHouse can now schedule tasks to run asynchronously, such as the sending of emails and notifications. I didn't mean to implement queues, but `django-ses` seems to hang the application while waiting for a response from AWS SES. I considered changing the Django deployment to ASGI (Asynchronous Server Gateway Interface) and redeclaring some of the view functions as `async def`...but this seemed like a bigger project than I wanted to take on, especially just to add email capabilities. So task queues are the solution!
