FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copier le projet
COPY pyproject.toml uv.lock ./

ENV UV_COMPILE_BYTECODE=1 \
    UV_FROZEN=1 \
    UV_LINK_MODE=copy \
    UV_NO_INSTALLER_METADATA=1 \
    VIRTUAL_ENV=/app/.venv \
    PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev
ENV PATH="/app/.venv/bin:$PATH"

COPY docker /app

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Lancer FastAPI
COPY docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]