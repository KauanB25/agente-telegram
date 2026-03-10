from sqlalchemy import create_engine, Engine


def create_engine_postgre(
        username,
        secret,
        host,
        database,
        driver,
        port=5432) -> Engine:

    url_db = f"{driver}://{username}:{secret}@{host}:{port}/{database}"

    engine = create_engine(url_db)

    return engine
