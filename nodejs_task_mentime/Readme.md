Aims and Objectives:
------------------

The objective of the solution is to develop Frontend and backend services, where frontend service with the implementation to query Restful API Endpoints and plot the bar graph according to the data(JSON) received. Complementarily, Backend service is responsible for developing Restful Endpoints and exposing them. In the SDLC(Software Development Life Cycle) both frontend and backend services are maintained in version control systems like GitHub, CI/CD Pipelines are maintained for building and Deploying services, and the platform team accomodate services with resources as it scales.


Tradeoffs in Implementation:
---------------------------
**Frontend service** has been developed as a static website. Tools used: HTML, CSS, JavaScript, ChartJS, Bootstrap. In the implementation, rather than creating dependencies to run static sites, all the dependencies like ChartJS, Bootstrap are embedded within the Javascript tag in the index.html page By using Minifiers. 
Containers are used to wrap bar plots within the HTML page. Implementation to call Restful API endpoints and Scrape the data(JSON) of interest is written in the "main.js" file.

Similarly, for the **Backend service** Node web Server with the implementation to expose Restful API Endpoints has been developed.
**Dockerizing** of node server has been done and is hosted at https://hub.docker.com/r/nasirali568/mentimet-node-server

Shortcuts chosen in the implementation:
-------------------------------------
Rather than **reinventing the wheel** it would be a great approach to spend some time investigating tools/Modules available for our use case.

For Developing frontend Application "ChartJS" Module/library was selected as a choice. There were several tools available for the same purpose, like "CanvasJSChart", "plotly.js" etc. but "ChartJS" was chosen because of its variety of chart types, Simplicity, Good Documentation(subjective). Lambda functions(anonymous functions) are used to minimize repetitive "for" loops with forEach.

Similarly, for Developing backend Applications, packages like express, cors are used. Such to make API communication smooth and robust.


Main Things Missing to go to production:
---------------------------------------
To comply with production grade Applications, the frontend service should be containerized, load balanced (using Reverse proxy), Hypervised (kubernetes or openshift etc), hosted with robust CI/CD Pipelines such each change gets into action quickly with best deployment strategies. 

Similarly, for Backend service: Firstly, make node server could update without having to reboot the container/service. It is achievable by using "nodemon" utility while Running container/application and it would require corresponding packages to import. then, to grow and shrink such to serve users, it should have all the above features mentioned for the frontend service.

To make it ready for production we need to replace logic to pull questions and answers with specific code from api endpoints instead of reading it from a static file in current implementation.



