AWS Services
----------------------------------------
1. EC2(Amazone Elastic Comput Cloud)
   
   EC2 is a virtual server in the AWS Cloud.
   It allows users to rent virtual servers, also known as instances, on which they can run their own applications. EC2 provides scalable computing capacity in the cloud, allowing users to quickly scale up or down the number of instances they use based on demand.
   Offers OS-level and hardware control, with automatic updates.
2.  Snowball
   
    Small device for transferring terabytes of data in/out of AWS.
3. CloudWatch
   
   Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time.
   Monitors AWS resources like RDS, EC2, and S3. Tracks metrics (e.g., CPU usage) and triggers alarms.
4. Elastic Transcoder
   
   Elastic Transcoder is a cloud-based AWS service that converts media files from one format to another.
5. VPC

   VPC can be referred to as the private cloud inside the cloud. It is a logical grouping of servers in a specified network. The servers that you are going to deploy in the Virtual Private Cloud(VPC) will be completely isolated from the other servers that are deployed in the Amazon Web Services.
6. Amazone S3
   
   Amazon S3 is a Simple Storage Service in AWS that stores files of different types like Photos, Audio, and Videos as Objects providing more scalability and security to. It allows the users to store and retrieve any amount of data at any point in time from anywhere on the web. It facilitates features such as extremely high availability, security, and simple connection to other AWS Services.

   Amazone S3 Types of storage classes are as follows:

   S3 Standard – The default storage class. If you don't specify the storage class when you upload an object, Amazon S3 assigns the S3 Standard storage class.
   S3 Express One Zone
   Reduced Redundancy – The Reduced Redundancy Storage (RRS) storage class is designed for noncritical, reproducible data that can be stored with less redundancy than the S3 Standard storage class.

   S3 Standard: The Go-to for Frequently Accessed Data. It is used for general purposes and offers high durability, availability, and performance object storage for frequently accessed data.(comes under Storage classes for frequently accessed objects)
   S3 IA(Infrequent Access): Amazon S3 IA is designed for the data which requires less frequent access, but with longer storage time than in the case of S3 Standard.
   Amazone Glacier: The S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive storage classes are designed for low-cost, long-term data storage and data archiving. These storage classes require minimum storage durations and retrieval fees making them most effective for rarely accessed data.

   Instance:Instances are virtual machines (VMs) that run in the cloud, and T2 and T3 are types of instances that provide a balance of CPU, RAM, storage, and networking capabilities.
   T2 instances are burstable, meaning their CPU performance can be scaled up and down. T3 instances are general-purpose and provide more consistent performance.

   A key pair, consisting of a public key and a private key, is a set of security credentials that you use to prove your identity when connecting to an Amazon EC2 instance.

Cloud Types:Public, Private, Hybrid.

Cloud Hierarchy
  SaaS (e.g., Gmail, Slack).
  DaaS (e.g., Urban Mapping).
  PaaS (e.g., MS 365, Zendesk).
  IaaS (e.g., AWS, Azure).
  FaaS: Manages and runs app microservices.
  IDaaS: Authentication-focused cloud services.

Auto Scaling in AWS:

  Auto Scaling is a service that automatically scales AWS resources to optimize application performance and costs.

Key Components of Auto Scaling:

  ASG (Auto Scaling Groups): Defines the capacity of instances.

Launch Configurations/Templates: Newly launched instances automatically inherit configurations within the ASG.

  Scaling Policies: Sets rules for scaling in or out (e.g., CPU usage, custom metrics).

Health Checks: Ensures instances remain healthy.

  Example: When demand increases, additional instances are added automatically and removed when demand decreases.

Load Balancer in AWS

  AWS Service: Distributes traffic across multiple instances.

Types of Load Balancers:

  ALB (Application Load Balancer): Operates at Layer 7 (Application Layer). Best for HTTP/HTTPS traffic with host/path-based routing.
    
  NLB (Network Load Balancer): Operates at Layer 4 (Transport Layer). Handles TCP and UDP traffic.
    
  CLB (Classic Load Balancer): Operates at both Transport and Application Layers.

Hybrid Cloud Architecture

  Hybrid Cloud: Combines public and private clouds.

  Public Cloud: Shared resources.

  Private Cloud: Confidential workloads.

EC2 Instances with Private IPs

  Service: VPC (Virtual Private Cloud).

  Allows launching EC2 instances with predetermined private IPs.

Data Transfer Solution

  Service: Amazon Snowball.

  Used for securely transferring petabytes of data in/out of AWS.

IAM Group Policy Management

To apply policies to multiple users without individual configuration:
Use AWS IAM Groups.

Add users to groups based on roles and apply policies to the group.
