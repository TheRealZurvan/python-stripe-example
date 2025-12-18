# Python Stripe Integration Example

This project demonstrates how to integrate Stripe payments into a Python application using the `stripe` library and `pydantic-settings` for configuration management.

## Prerequisites

- [Python 3.14.2](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) (recommended)
- [mise](https://mise.jdx.dev/) (optional, for task running)
- A [Stripe account](https://stripe.com/) and API keys

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python-stripe-example
   ```

2. **Install dependencies:**
   Using `uv`:
   ```bash
   uv sync
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory based on the `.env.example` (if available) or with the following content:
   ```env
   STRIPE_SECRET_KEY=your_stripe_secret_key
   PAYMENT_SUCCESS_URL=http://localhost:8000/success
   PAYMENT_CANCEL_URL=http://localhost:8000/cancel
   ```

## Usage

You can run the example script using `mise` or directly with `uv`.

### Using mise
```bash
mise run main
```

### Using uv
```bash
uv run src/main.py
```

The script will create a Stripe Checkout Session for a "Philosopher's Stone" and print the session object to the console.

## Project Structure

- `src/main.py`: The main entry point that creates a Stripe Checkout Session.
- `src/config.py`: Configuration management using `pydantic-settings`.
- `pyproject.toml`: Project dependencies and metadata.
- `mise.toml`: Task runner configuration.
