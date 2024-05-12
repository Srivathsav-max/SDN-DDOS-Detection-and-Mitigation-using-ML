# SDN-DDOS-Detection-and-Mitigation-using-ML

This repository contains the setup and code for a project that uses Software Defined Networking (SDN) to detect and mitigate Distributed Denial of Service (DDoS) attacks. The project utilizes tools such as the Ryu controller, Mininet, and hping3, managed with Python 2 due to Ryu's dependencies.

## Prerequisites

Ensure you are using Ubuntu 20.04.1.4 LTS with internet access.

## Installation Guide

### Update System Packages
Start by updating your system's package list and install the latest versions of the packages:
```bash
sudo apt update
sudo apt upgrade -y
```

### Install Git
Install Git to clone the repository:
```bash
sudo apt install git -y
```

### Clone the Project Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Srivathsav-max/SDN-DDOS-Detection-and-Mitigation-using-ML.git
```

### Install Python 2
Install Python 2, as it is required by the Ryu controller:
```bash
sudo apt install python2 -y
```

### Install Ryu Controller
Install the Ryu controller, which is a component necessary for SDN programming:
```bash
sudo apt install python-pip -y
pip install ryu
```

### Install Mininet
Install Mininet, which is used to simulate the network:
```bash
sudo apt install mininet -y
```

### Install hping3
Install hping3, a tool used for generating network traffic:
```bash
sudo apt install hping3 -y
```

## Running the Project
To run the project, navigate to the cloned directory, and execute the scripts or commands as defined in your project documentation.

### To Generate Dataset
change `TEST_TYPE` in `topo.py` to normal or attack to generate data to generate packets accordingly make sure you need to change `controller.py` `APP_TYPE` to `0` to collect data and `1` to enable ddoss mitigate model

### Run the Controller
To start the Ryu controller with your custom script, use the following command:
```bash
ryu-manager controller.py
```

### Run Mininet Topology
To initiate the Mininet topology, use:
```bash
sudo python2 topo.py
```

### Clean Up Mininet
After any changes to topology script, ensure to clean up the Mininet environment:
```bash
sudo mn -c
```
