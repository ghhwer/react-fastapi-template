# Backend

## Overview

This directory contains the backend implementation of {Your Project}, {Description of your project}. 
The backend is built using FastAPI backed by DuckDB and managed with UV as the package manager.

## Getting Started

### Prerequisites

* UV installed on your system. For installation instructions, refer to the [UV documentation](https://docs.astral.sh/uv/).

### Installation and Running the Application

1. Install the dependencies:
```bash
uv sync
```
2. Run the application with auto-reload:
```bash
uv run uvicorn main:app --reload
```

## Development

* The application logic is contained within the `main.py` file.
* Configuration and dependencies are managed through UV.

## Notes

* Make sure to check the UV documentation for more information on managing dependencies and environments.