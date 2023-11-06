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
      latitude VARCHAR(255),
      longitude VARCHAR(255),
      physical_address VARCHAR(255)
    );

    -- Создание второй таблицы
    CREATE TABLE dataset_db (
      id SERIAL PRIMARY KEY,
      file_name VARCHAR(255),
      full_file_path VARCHAR(255),
      class_number INTEGER,
      labels_path VARCHAR(255)
    );

    -- Создание третьей таблицы
    CREATE TABLE employee_db (
      id SERIAL PRIMARY KEY,
      FIO VARCHAR(255),
      day_password VARCHAR(255),
      UNIQUE (id)
    );
