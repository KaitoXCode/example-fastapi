from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str  # = os.environ['DATABASE_HOSTNAME']
    database_port: str  # = os.environ['DATABASE_PORT']
    database_password: str  # = os.environ['DATABASE_PASSWORD']
    database_name: str  # = os.environ['DATABASE_NAME']
    database_username: str  # = os.environ['DATABASE_USERNAME']
    secret_key: str  # = os.environ['SECRET_KEY']
    algorithm: str  # = os.environ['ALGORITHM']
    access_token_expire_minutes: int  # = os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']

    class Config:
        env_file = '.env.py'
        env_file_encoding = 'utf-8'


settings = Settings()


