    CREATE USER postgre_user WITH PASSWORD '123';
    CREATE  database LoDTGunDetect
    WITH OWNER postgre_user
    TEMPLATE = 'template0'
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.utf8'
    LC_CTYPE = 'ru_RU.utf8';
    GRANT ALL PRIVILEGES ON DATABASE LoDTGunDetect TO postgres;

    --Создание первой таблицы
    CREATE TABLE camera_db (
      id SERIAL PRIMARY KEY,
      urls VARCHAR(15),
      latitude VARCHAR(255) NULL,
      longitude VARCHAR(255) NULL,
      physical_address VARCHAR(255) NULL
    );
