# 🚀 Interactive Spiral Visualization with Streamlit

Welcome to the **Streamlit Dashboard** project! This interactive app lets you visualize and manipulate a dynamic spiral using just a few sliders. Built with **Streamlit**, **Altair**, and **Python**, this project is a perfect example of how simple code can create stunning visualizations.

---

## 🎨 Features
- **Dynamic Spiral Control** – Adjust the number of points and turns using sliders.
- **Real-time Visualization** – Instantly updates the spiral based on your inputs.
- **Beautiful & Responsive UI** – Powered by **Altair** and **Streamlit**.
- **One-click Deployment** – Easily deploy your own version on Streamlit Cloud.
- **Docker Support** – Containerize your app for consistent environments.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Tanmay-hue/Streamlit_Dashboard.git
cd Streamlit_Dashboard
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app locally
```bash
streamlit run spiral_app.py
```

This will launch the dashboard in your default web browser! 🎉

---

## 📦 Docker Deployment

If you prefer using Docker for a consistent development and deployment environment, follow these steps:

### Dockerfile Example
Create a file named `Dockerfile` in the root of your project with the following content:

```dockerfile
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt . 
RUN python -m pip install -r requirements.txt

WORKDIR /code
COPY . /code

# During debugging, this entry point will be overridden.
CMD ["streamlit", "run", "spiral_app.py"]
```

### Building and Running the Docker Container
1. **Build the Docker image:**
   ```bash
   docker build -t streamlit-dashboard .
   ```
2. **Run the Docker container:**
   ```bash
   docker run -p 8501:8501 streamlit-dashboard
   ```
Your app will now be accessible at `http://localhost:8501`.

---

## 📡 Deploying to Streamlit Cloud

Want to make your app accessible online? Follow these steps:
1. Push your code to **GitHub**.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New App** ➝ Select your repo ➝ Choose `spiral_app.py`.
4. Click **Deploy** and get your own shareable link! 🚀

---

## 📸 Preview
![Spiral Preview](https://github.com/Tanmay-hue/Streamlit_Dashboard/blob/main/image.png)

Experience the magic of interactive visualizations with just a few lines of code! 🌀

---

## 📌 Tech Stack
- **Streamlit** - For building interactive dashboards
- **Altair** - For elegant data visualizations
- **Pandas** - For efficient data handling
- **Python** - The powerhouse behind the logic
- **Docker** - For containerized deployments


---

Happy coding! 🎨✨

By - Tanmay Singh
