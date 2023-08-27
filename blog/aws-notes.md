# AWS Cheatsheet

August 2023

## Compute Services

`ECR` - Elastic Container Registry, stores images (e.g. Docker)  
`ECS` - Elastic Container Service, orchestrates/scales Docker containers  
`EC2` - Elastic Compute Cloud, virtual machine. Rent in cloud. Common use case is as a server for a web application. Do whatever on it though  
`Load Balancing` - Allows traffic to be distributed among multiple EC2 instances  
`Cloud Watch` - collects logs and metrics from EC2 instances  
`Auto Scaling` - defines policies to create new EC2 instances based on traffic, etc  
`Elastic Beanstalk` - More abstraction on top of EC2 and all the above services (aka PaaS - Platform as a Service)  
`Lightsail` - Even more abstraction...  
`Lambda` - Functions as a Service, aka Serverless. Code runs only when an event occurs. Only pay for requests and compute time, not constant uptime  
`Serverless Repo` - more abstraction on top of a Lambda  
`Outposts` - Runs AWS APIs on your personal server  

## General-Purpose Storage  

`Snow` - mini data-centers that function without internet  
`ECR` - Elastic Container Registry, allows you to upload images (e.g. Docker)  
`ECS` - Elastic Container Service, starts and stops containers  
`Fargate` - Makes containers behave like serverless functions and run on demand (not constantly), so you don't need to run an EC2 full-time  
`S3` - Simple Storage Service, stores any data. Good for general purpose file storage  
`Glacier` - lower cost version of S3, higher latency  
`Block Storage` - higher cost version of S3, lower latency  
`Elastic File System` - higher abstraction, higher cost  

## Database Services  

`Simple DB` - General purpose NOSQL database  
`Dynamo DB` - document-style database, more sophisticated, higher cost  
`Document DB` - Behaves exactly like MongoDB  
`Elastic Search` - for constructing a search engine  
`RDS` - Relational Database Service, SQL service  
`Aurora` - another db service, allows for serverless (runs on trigger, not constantly up)  
`Neptune` - graph database  
`Elastic Cache` - Redis implementation  
`TimeStream` - time-series database  

## Analytics  

`Redshift` - data warehouse, alternative to Oracle, query with SQL  
`Lake Formation` - store large amounts of unstructured data  
`Kinesis` - analyze real-time data  
`Map Reduce` - operates on massive data sets in parallel  
`Glue` - Serverless, ETL (extract transform load) service for data  
`Data Exchange` - Purchase data from 3rd party sources  

## Machine Learning  

`Sagemaker` - Connect to data to implement ML models  
`Rekognition` - Image analysis  

## Dev Tools  

`IAM` - create rules, permissions  
`Cognito` - Handles authentication  
`Simple Notification Service` - push notifications to users  
`Simple Email Service` - email notifications to users  
