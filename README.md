# System Data Display Panel
### Overview:
This system is intended to be used on local networks for the purpose of displaying basic systems data on a single device.
The server collects system data from client devices on the network, and displays a browser GUI with a locally hosted HTTP request handler.

### Server System:
The server uses a python backend for client data handling and HTTP request handling.
The browser is provided with HTML and CSS and Javascript to display the interface and update it with provided data.
A JSON file is prepared in the backend and polled by the frontend to provide client data to be displayed.

At present, the intention is for the server to detect relivant API endpoints on its local network, and requiest data from there. This isn't scalable, and will be revised into a better solution.

### Client System:
The client runs a python script that collects system data such as CPU, GPU, and RAM load, disk usage, etc., formats it into JSON, and returns this data when requested. The client script hosts a Flask API endpoint that can be queried for the above data. There are no API safety systems presently implemented.

