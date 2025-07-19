# react-fastapi-template

This repository provides a quickstart template for creating applications using React for the frontend and FastAPI for the backend. It serves as an example application to demonstrate how to integrate these technologies.

## Project Purpose

The purpose of this project is to provide a basic template for building modern web applications with a React frontend and a FastAPI backend. This combination allows for a robust and scalable application architecture.

## Technologies Used

- **Frontend**: React
- **Backend**: FastAPI
- **Database**: [Insert database technology if applicable]

## Usage Instructions

### Prerequisites

- Node.js (for React frontend)
- Python (for FastAPI backend)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ghhwer/react-fastapi-template.git
   ```
2. Install frontend dependencies:
   ```bash
   cd frontend && npm install
   ```
3. Install backend dependencies:
   ```bash
   cd backend && uv sync
   ```
4. Start the backend server:
   ```bash
   cd backend && uv run uvicorn main:app --reload
   ```
. Start the frontend development server:
   ```bash
   cd frontend && npm run dev
   ```

### Code Structure

The project is divided into two main directories: `frontend` and `backend`.

- **Frontend**: Contains all React-related code, including components, pages, and global styles.
- **Backend**: Contains all FastAPI-related code, including routes, models, and database interactions.

## Contributing

Contributions are welcome. Please submit pull requests with a clear description of your changes.
