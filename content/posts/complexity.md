+++
title = 'Complexity'
date = 2024-06-04T23:21:19-06:00

draft = true
+++

The deployment of this website was changed a few months ago to run inside a container. The container was run on a Raspberry Pi 3 remote server, and HTTP requests were being routed using `nginx`. 

Why was this level of complexity needed for a simple static site? It turns out, it wasn't.

## The Journey

`mermaid diag of v1`

The v.1 deployment plan involved merely deploying the site using GitHub Actions and GitHub Pages. It was dirt simple and worked very reliably.

However, I became paranoid about my use of GoDaddy for DNS services. So I uprooted and migrated the domain to Mythic Beasts, which I decided was less sketchy. The downside is, Mythic Beasts UI is more complicated to navigate. No problem, I thought, this is a good opportunity for me to better understand how DNS works.

After some learning, I was able to get the domain wired up and the site was running again. So far, so good - no code had to change on the site. 

Next, I decided that manually rolling a website was getting cumbersome. For v.1, I had hand-written shell deployment scripts, and they were starting to get a little buggy. I had bandaged them together numerous times, but the scripts were just starting to fall apart beyond repair. I had learned most of what I could about the beauty of using 0 web frameworks, and also incurred some of the battle scars. It was time for an upgrade.

After some research, it appeared that one of the lightest possible frameworks I could get away with using for a static site was [Hugo](https://gohugo.io/). I began the migration process to Hugo, and was pleased to discover that I had functional Hugo site within a few evenings.

I decided I wanted to be more in control of my (deployment) destiny, and that GitHub Pages was ceding too much control to GitHub. In retrospect, this was an incorrect assessment. However, I made the decision at the time to `Docker`-ize the Hugo application, add `nginx` as a proxy service, and run the site on Raspberry Pi 3 remote server I purchased from Mythic Beasts. In this v.2 design, I had originally planned for one `nginx` service to run inside the Docker container, and to be able to handle HTTP requests that the Raspberry Pi received.

`mermaid diag of v2`

I was mistaken - after implementing this design, I realized that a second `nginx` service needed to be running outside of the container, on the Raspberry Pi itself. So the v.2 design had two `nginx` services proxying requests between each other. This was getting ugly, and buggy, quickly.

I soon became consumed with other projects, so some somewhat unacceptable site bugs lingered. The site was only accessible at `http://`, for example. Secure HTTP was not being proxied correctly by the dual `nginx` services. After finding some time revisit the setup, it appeared as if it could be bandaged together by updating the `nginx.conf` file inside the Docker container.

But this was incorrect. Since some months had gone by, I had forgotten about the second `nginx.conf` file lurking in `/etc/config/nginx/sites-available/ashwinsundar` on the Raspberry Pi. This file has been created manually and then forgotten about, since it didn't live in version control or my normal line-of-sight. After several hours of futile debugging of the Docker `nginx.conf`, I discovered this second config file...and decided that this was enough. It was time for a v.3.

`mermaid diag of current v3`

The goal of v3 was simple - back to basics. Rip out the duelling `nginx` services, Docker, and the arcane build steps I had written up every time I wanted to add a new post to the site. It was annoying to push a Docker image, pull it on the server, stop the old container, and rebuild the new one - just to fix a typo. I wanted to go back to the deployment process of v1 `git push` to main, and let GitHub Actions/Pages take care of the rest. This time, I swapped out GitHub for DigitalOcean for the deployment task. And it works!

There is still a little messiness. The DNS is configured in Mythic Beasts, so some trial-and-error was needed to get the records pointing to DigitalOcean's servers, where the Hugo app was actually being served. This could be further simplified by migrating domain ownership to DigitalOcean. But I'm happy to sit with this configuration, which works, and learn some more about DNS. Until it becomes painful again, at which point I'll migrate.

## Lessons Learned

- There are many ways to design a system. It's important to understand the tradeoffs.
- There are an unlimited number of ways to incorrectly design a system. Dual `nginx` services is one of them, for the use case of serving HTTP requests to a static site server.
- DNS configuration is less scary than I thought. Chapter X of Computer Networks by Andrew Tanenbaum is a good primer. I'm still no expert, but I'm less scared than I was before starting this process.
- There is a senior principal developer that lives behind my left ear and likes to whisper things that make me feel like an imposter. I learned to tune them out, and be okay with making mistakes in my free time. It makes life a little more interesting.