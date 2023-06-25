CREATE TABLE person
(
username TEXT NOT NULL PRIMARY KEY,
number INT NOT NULL,
address TEXT 
);

CREATE TABLE pet
(
firstname TEXT NOT NULL,
lastname TEXT NOT NULL,
birthdate INT,
PRIMARY KEY (firstname, lastname)
);

CREATE TABLE Dog(
firstname TEXT,
lastname TEXT,
breed TEXT,
PRIMARY KEY (firstname, lastname),
FOREIGN KEY (firstname, lastname) REFERENCES pet(firstname, lastname)
);

CREATE TABLE Snake(
firstname TEXT,
lastname TEXT,
venom TEXT,
PRIMARY KEY (firstname, lastname),
FOREIGN KEY (firstname, lastname) REFERENCES Pet(firstname, lastname)
);

CREATE TABLE Barked_at(
firstname_d TEXT,
lastname_d TEXT,
firstname_s TEXT,
lastname_s TEXT,
FOREIGN KEY (firstname_d, lastname_d) REFERENCES Dog(firstname, lastname),
FOREIGN KEY (firstname_s, lastname_s) REFERENCES Snake(firstname, lastname)
);

CREATE TABLE Play_Friend(
firstname_to TEXT,
lastname_to TEXT,
firstname_from TEXT,
lastname_from TEXT,
since DATE,
FOREIGN KEY (firstname_to, lastname_to) REFERENCES Pet(firstname, lastname),
FOREIGN KEY (firstname_from, lastname_from) REFERENCES Pet(firstname, lastname)
);

CREATE TABLE Seller(
username TEXT,
firstname TEXT,
lastname TEXT,
FOREIGN KEY (firstname, lastname) REFERENCES pet(firstname, lastname),
FOREIGN KEY (username) REFERENCES person(username),
PRIMARY KEY(username, firstname, lastname)
);

CREATE TABLE Owner(
username TEXT,
firstname TEXT,
lastname TEXT,
FOREIGN KEY (firstname, lastname) REFERENCES pet(firstname, lastname),
FOREIGN KEY (username) REFERENCES person(username),
PRIMARY KEY(username, firstname, lastname)
);