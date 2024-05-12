CREATE TABLE Users (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	fname TEXT(64) NOT NULL,
	lname TEXT(64),
	phone TEXT(11) NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE Reached (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"timestamp" TEXT NOT NULL, user_id INTEGER NOT NULL,
	CONSTRAINT user_id FOREIGN KEY (id) REFERENCES Users(id)
);