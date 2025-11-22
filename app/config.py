# Compatibility for pydantic v1 and v2.
# Decide pydantic major version first, then define Settings accordingly.

# Determine pydantic major version robustly
try:
    import pydantic as _pyd
    _pv = getattr(_pyd, "__version__", "2.0.0")
    _pyd_major = int(_pv.split(".")[0])
except Exception:
    # If anything unexpected, assume v2 behavior
    _pyd_major = 2

IS_PYDANTIC_V2 = _pyd_major >= 2

if IS_PYDANTIC_V2:
    # pydantic v2 + pydantic-settings
    try:
        from pydantic_settings import BaseSettings
    except Exception:
        # fall back to BaseSettings from pydantic if available (best-effort)
        from pydantic import BaseSettings
    from pydantic import Field

    class Settings(BaseSettings):
        APP_ENV: str = Field("development", env="APP_ENV")
        SECRET_KEY: str = Field("please-change-me", env="SECRET_KEY")
        DATABASE_URL: str = Field("sqlite:///./test.db", env="DATABASE_URL")
        REDIS_URL: str = Field("redis://localhost:6379/0", env="REDIS_URL")

        # Postgres settings (declare these so env vars aren't treated as "extra")
        POSTGRES_USER: str = Field("taskmaster", env="POSTGRES_USER")
        POSTGRES_PASSWORD: str = Field("taskmaster", env="POSTGRES_PASSWORD")
        POSTGRES_DB: str = Field("taskmaster_db", env="POSTGRES_DB")
        POSTGRES_HOST: str = Field("db", env="POSTGRES_HOST")
        POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")

        # pydantic v2 uses model_config dict instead of class Config
        model_config = {
            "extra": "ignore",
            "env_file": ".env",
            "env_file_encoding": "utf-8",
        }

else:
    # pydantic v1
    from pydantic import BaseSettings, Field

    class Settings(BaseSettings):
        APP_ENV: str = Field("development", env="APP_ENV")
        SECRET_KEY: str = Field("please-change-me", env="SECRET_KEY")
        DATABASE_URL: str = Field("sqlite:///./test.db", env="DATABASE_URL")
        REDIS_URL: str = Field("redis://localhost:6379/0", env="REDIS_URL")

        # Postgres settings (declare these so env vars aren't treated as "extra")
        POSTGRES_USER: str = Field("taskmaster", env="POSTGRES_USER")
        POSTGRES_PASSWORD: str = Field("taskmaster", env="POSTGRES_PASSWORD")
        POSTGRES_DB: str = Field("taskmaster_db", env="POSTGRES_DB")
        POSTGRES_HOST: str = Field("db", env="POSTGRES_HOST")
        POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")

        class Config:
            env_file = ".env"
            env_file_encoding = "utf-8"
            extra = "ignore"