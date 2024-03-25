CREATE TABLE IF NOT EXISTS Жанр (
	Id SERIAL PRIMARY KEY,
	Название varchar(40)
);

CREATE TABLE IF NOT EXISTS Исполнитель (
	Id SERIAL PRIMARY KEY,
	Псевдоним VARCHAR(60)
);

CREATE TABLE IF NOT EXISTS Жанр_Исполнитель (
	Жанр_id INTEGER REFERENCES Жанр(Id),
	Исполнитель_id INTEGER REFERENCES Исполнитель(Id),
	CONSTRAINT Ж_И PRIMARY KEY (Жанр_id, Исполнитель_id)
);

CREATE TABLE IF NOT EXISTS Альбом (
	Id SERIAL PRIMARY KEY,
	Название VARCHAR(60) NOT NULL,
	Год_выпуска date NOT NULL
);

CREATE TABLE IF NOT EXISTS Исполнитель_Альбом (
	Альбом_id INTEGER REFERENCES Альбом(Id),
	Исполнитель_id INTEGER REFERENCES Исполнитель(Id),
	CONSTRAINT А_И PRIMARY KEY (Альбом_id, Исполнитель_id)
);

CREATE TABLE IF NOT EXISTS Трек (
	Id SERIAL PRIMARY KEY,
	Название VARCHAR(40),
	Длительность VARCHAR(10),
	Альбом_id INTEGER NOT NULL REFERENCES Альбом(id)
);

CREATE TABLE IF NOT EXISTS Сборник (
	Id SERIAL PRIMARY KEY,
	Название VARCHAR(60) NOT NULL,
	Год_выпуска DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Состав_сборника (
	Трек_id INTEGER REFERENCES Трек(Id),
	Сборник_id INTEGER REFERENCES Сборник(Id),
	CONSTRAINT Т_С PRIMARY KEY (Трек_id, Сборник_id)
);

--25.03.2024 14:42
ALTER TABLE Жанр ADD UNIQUE (Название);
ALTER TABLE Жанр ALTER COLUMN Название SET NOT NULL;
ALTER TABLE Исполнитель ALTER COLUMN Псевдоним SET NOT NULL;
ALTER TABLE Трек ALTER COLUMN Название SET NOT NULL;
ALTER TABLE Трек ALTER COLUMN Длительность SET NOT NULL;
ALTER TABLE Исполнитель ADD UNIQUE (Псевдоним);
ALTER TABLE Альбом ADD UNIQUE (Название);