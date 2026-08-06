# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI tutorial project demonstrating FastAPI and Pydantic usage. The project uses `uv` for dependency management and includes example implementations of type hints, Pydantic models, and FastAPI endpoints.

## Development Commands

### Setup and Running

```shell
# Install dependencies
uv sync

# Run the FastAPI development server with auto-reload
uv run uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000 with interactive docs at http://127.0.0.1:8000/docs

## Architecture

### Project Structure

- **main.py**: FastAPI application entry point with REST endpoints
  - Contains the `Item` Pydantic model used for request/response validation
  - Implements POST `/items/` and GET `/items/` endpoints

- **pydantic_demo.py**: Standalone Pydantic validation examples
  - Demonstrates Pydantic's `BaseModel` usage, validation error handling, and data parsing
  - Includes `User` model with datetime and constraint validation examples

- **tutorial_types.py**: Python type hint examples and utility functions
  - Basic typing examples without FastAPI/Pydantic dependencies

### Key Dependencies

- **FastAPI**: Web framework (v0.120.3+)
- **Pydantic**: Data validation using Python type annotations (v2.12.3+)
- **uv**: Package and project manager (configured to use Tsinghua PyPI mirror)

### Python Version

Requires Python >= 3.11 (uses modern union type syntax like `str | None`)
