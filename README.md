# MedSync AI

MedSync AI is a comprehensive healthcare management platform featuring a modern React frontend and a FastAPI backend with AI workflow integration. 

## 🚀 Quick Start (Local Development)

This project requires both the backend API and the frontend application to be running simultaneously.

### 1. Backend Setup (FastAPI)

The backend is built with Python, FastAPI, and SQLAlchemy.

1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   - **Windows:** `python -m venv venv && .\venv\Scripts\activate`
   - **Mac/Linux:** `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   *The API will be available at `http://localhost:8000`. You can view the interactive API documentation at `http://localhost:8000/docs`.*

### 2. Frontend Setup (React + Vite)

The frontend is a React Single Page Application (SPA) built with Vite and TailwindCSS.

1. Open a **new** terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *The frontend will be available at `http://localhost:5173`. Open this URL in your browser.*

## 🌍 Production Deployment (Vercel)

This repository is pre-configured for a seamless deployment on Vercel. 

### Vercel Settings
When importing this project into Vercel, use the following configuration:
- **Framework Preset**: Vite
- **Build Command**: `cd frontend && npm install && npm run build`
- **Output Directory**: `frontend/dist`
- **Root Directory**: `./` (Keep default, do not change to `frontend`)

### Required Environment Variables
Ensure the following variables are set in your Vercel Project Settings:
- `VITE_API_BASE_URL` (For the frontend)
- `DATABASE_URL` (Postgres URL for production, as SQLite is ephemeral on Vercel)
- `SECRET_KEY` (Random string for JWT authentication)

## 📁 Repository Structure

- `/frontend` - React Application (Vite, TailwindCSS, React Router)
- `/backend` - Python API (FastAPI, LangChain, SQLite/PostgreSQL)
- `api/index.py` - Vercel Serverless Function entry point
- `vercel.json` - Vercel deployment routing and configuration
