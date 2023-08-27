# Web Infrastructure Design:

## 1. User Accessing the Website:

A user types "www.foobar.com" in their web browser.

## 2. DNS Resolution:

The DNS resolves "www.foobar.com" to the IP addresses of the load balancer.

## 3. Load Balancer (HAproxy):

Servers: Server1 (8.8.8.8), Server2 (8.8.8.9)
HAproxy distributes incoming traffic between servers. It helps improve performance and provides redundancy.

## 4. Firewalls:

Firewalls are added to protect the servers from unauthorized access. They filter incoming and outgoing network traffic, blocking potential threats.

## 5. Nginx Web Server with SSL:

Servers: Server1 (8.8.8.8), Server2 (8.8.8.9)
Nginx serves as a reverse proxy and handles SSL termination. SSL certificates are used to encrypt data in transit, enhancing security.

## 6. Application Server:

Servers: Server1 (8.8.8.8), Server2 (8.8.8.9)
The application server processes requests, communicates with the database, and generates dynamic content.

## 7. MySQL Database Cluster:

Servers: Primary/Master (8.8.8.10), Replica/Slave (8.8.8.11)
The database cluster improves availability. Primary handles writes, and changes are replicated to the Replica for redundancy.

## 8. Monitoring Clients (Sumo Logic):

Monitoring clients collect data on server performance. This data is sent to Sumo Logic or another monitoring service for analysis.

## 9. Application Logic:

The application server executes the logic of your website, handling user requests, querying the database, and generating dynamic content.

## 10. Response Generation:

The application server sends the generated content back to the Nginx server.

## 11. Nginx Response:

Nginx receives content from the application server and returns it in the form of an HTTP response to the user's browser.

## 12. User's Browser:

The user's browser renders the received content and displays the website.

## 13. Firewalls:

Firewalls are added for security. They filter incoming and outgoing traffic, safeguarding the servers from unauthorized access and potential attacks.

## 14. SSL Certificate:

HTTPS is used to encrypt data between the server and the user's browser, enhancing privacy and security.

## 15. Monitoring:

Monitoring tools collect and analyze data about server performance, availability, and potential issues.


# Issues with the Enhanced Infrastructure:

## Terminating SSL at Load Balancer:

Terminating SSL at the load balancer might be an issue as the traffic between the load balancer and the application servers could be unencrypted, potentially exposing sensitive data.

## Single MySQL Server Accepting Writes:

Having only one MySQL server that accepts writes is a single point of failure. If this server fails, write operations would be disrupted.

## Uniform Servers with Same Components:

Uniform servers might be problematic as a failure in a common component (e.g., database) would impact all servers. Variability in components could provide redundancy.
