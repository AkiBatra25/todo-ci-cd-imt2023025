# CI/CD Pipeline – To-Do CLI Application (IMT2023025)

This repository contains a simple **Python-based To-Do List CLI** application created for the Software Engineering Lab CI/CD assignment.  

A complete CI/CD pipeline is implemented using:

- **GitHub** – Source code hosting  
- **Jenkins** – Automated build, test & deployment pipeline  
- **Docker** – Containerization of the application  
- **Docker Hub** – Hosting the built Docker image  

---

## 📌 Project Structure

imt2023025-todo-ci-cd
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md

---

## 🔄 CI/CD Pipeline Stages (Automated using Jenkins)

### **1️⃣ Checkout Code**
Jenkins pulls the latest code from GitHub.

### **2️⃣ Install Dependencies**
Uses pip to install Python packages from `requirements.txt`.

### **3️⃣ Run Unit Tests**
Executes all tests via **pytest**.  
If tests fail → pipeline stops → Docker image will NOT be built.

### **4️⃣ Build Docker Image**
If tests pass, Jenkins builds the image using:

akibatra25/imt2023025-todo


### **5️⃣ Push to Docker Hub**
Jenkins logs in to Docker Hub and pushes the image to:

👉 https://hub.docker.com/r/akibatra25/imt2023025-todo

---

## 🐳 Running the Docker Image

After the image is pushed, the To-Do CLI can be run using:

```bash
docker run -it akibatra25/imt2023025-todo
🧪 Running Tests Locally
Install packages:


pip install -r requirements.txt
Run tests:

pytest
🔧 Jenkins Setup Details
The pipeline uses:

Source: Pipeline script from SCM

Branch: main

Script Path: Jenkinsfile

Docker Hub credentials stored in Jenkins:


ID: dockerhub-creds-3025
Used by Jenkinsfile to authenticate and push.

📁 Docker Hub Repository Link
🔗 https://hub.docker.com/r/akibatra25/imt2023025-todo

👤 Author
Akshat Batra
Roll Number: IMT2023025

