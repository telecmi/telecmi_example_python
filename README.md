# TeleCMI Webhook Python

TeleCMI webhooks implementation in python. Use our simple python web server to test your webhooks and live events locally for development purpose.

## Install

Follow the below installation instructions

### Prerequisites

Prerequisites for python web server.

- <a href="https://git-scm.com/" target="_blank">git</a> (>= 2.20.1 required)
- <a href="https://www.python.org/" target="_blank">python</a> (>= 2.7.16 required)
- <a href="https://pypi.org/project/pip/" target="_blank">pip</a> (>= 18.1 required)


### Clone the repository

Use command __git clone__ to clone the python webserver from our <a href="https://github.com/telecmi/telecmi_example_python" target="_blank">TeleCMI github repository</a>.

```bash
$ git clone https://github.com/telecmi/telecmi_example_python.git
$ cd telecmi_example_python
```
### Install flask package using pip

Use command __pip__ to install the flask(lightweight web application framework).

```bash
$ pip install flask # shows the tagged versions
```


## Run

Run your python server using the below command

```bash
$ python webhooks.py
```
Now you can able to test our webhooks and live events, from your local server. To expose your local web server to the internet use ngrok. 

You can create a secure HTTP tunnel by providing the port number on which your web server is running. For example, your web server is running on port number 5000. you can launch your HTTP tunnel with the following command line.

```bash
$ ./ngrok http 5000
```

After exposing your local webserver to the internet using ngrok you will get the following output.

```bash
ngrok by @inconshreveable                                       (Ctrl+C to quit)
                                                                                
Session Status                online                                            
Session Expires               7 hours, 59 minutes                               
Update                        update available (version 2.3.35, Ctrl-U to update
Version                       2.3.34                                            
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    http://c654b286.ngrok.io -> http://localhost:5000 
Forwarding                    https://c654b286.ngrok.io -> http://localhost:5000
                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90       
                              0       0       0.00    0.00    0.00    0.00  
```
Now you can get your dynamic URL from the above output. To configure webhooks and live events, paste your dynamic URL with correct path in webhooks section.

#### Sample URL with path
```
http://c654b286.ngrok.io/webhook/cdr
```



