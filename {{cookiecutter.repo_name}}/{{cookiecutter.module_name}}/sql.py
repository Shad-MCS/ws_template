"""
Functionality to interface with SQL.

Delete if not used.
"""

import json
import sqlalchemy as sa
import boto3


def get_credentials(secret_name: str) -> dict:
    """Get credentials from secrets manager."""
    session = boto3.session.Session()  # type: ignore
    secret_client = session.client(
        service_name="secretsmanager", region_name="us-east-1"
    )
    secrets = json.loads(
        secret_client.get_secret_value(SecretId=secret_name)["SecretString"]
    )
    return secrets


def database_connection(secret_name: str) -> sa.Engine:
    """Wrapper function for getting credentials and creating a SQLAlchemy engine."""
    creds = get_credentials(secret_name=secret_name)
    engine = create_engine(creds)
    return engine


def create_engine(secrets: dict) -> sa.Engine:
    """Creates a SQLAlchemy Engine from a dictionary of secrets."""
    try:
        dbhost = secrets["host"]
        dbuser = secrets["username"]
	dbport = secrets["port"]
        dbpassword = secrets["password"]
        dbdatabase = secrets["dbname"]
        engine = sa.create_engine(
            f"postgresql://{dbuser}:{dbpassword}@{dbhost}:{port}/{dbdatabase}"  # noqa
        )
        return engine
    except Exception as e:
        raise (e)
