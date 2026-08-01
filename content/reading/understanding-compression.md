+++
title = "Understanding Compression - McAnlis and Haecky (2016)"
date = 2026-08-01
genres = ["reading", "2026"]
draft = false
+++

While at Big Sky Dev Conf last weekend, I heard a great talk which was a primer on compression techniques by Lance Fisher. The approachability of this topic, not to mention the wonderful application of information theory and math, nerd-sniped me to purchase this book and try to learn more about a topic that I have little experience with. 

Compression techniques abound in computing - it's one of the invisible abstractions that underlies data transmission. The less data you need to transfer, the faster it can be transfered, the cheaper it can be transfered...you get the picture. 

My only encounter with compression was when looking at ways to reduce how much data was being sent over the wire for hypermedia responses in MouseHouse. I was curious as to whether the payloads were being compressed, and learned about how the data was already being compressed using `gzip`. This can be inspected in the payload by looking for a response header called `Content-Encoding`. I started looking into `Brotli` compression before concluding that I don't understand compression well enough to make an intelligent decision to change the default compression method.

Several months later, I hear Lance's talk and this excursion into HTTP compression comes back to me. 
