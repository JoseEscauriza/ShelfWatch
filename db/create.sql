DROP TABLE IF EXISTS status CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS member CASCADE;
DROP TABLE IF EXISTS author CASCADE;
DROP TYPE IF EXISTS state;

CREATE TYPE state AS ENUM('pending', 'reading', 'complete');

CREATE TABLE member (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modification_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    author_first_name VARCHAR(50),
    author_last_name VARCHAR(50) NOT NULL,
    author_birthdate DATE
);

CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    author_id INT,
    title varchar(50) NOT NULL,
    description TEXT,
    genre VARCHAR(50) NOT NULL,
    creation_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (author_id) REFERENCES author (id)
);

CREATE TABLE status (
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    status state DEFAULT 'pending',
    pct_read SMALLINT NOT NULL DEFAULT 0,
    start_date DATE,
    end_date DATE,

    PRIMARY KEY (member_id, book_id),
    FOREIGN KEY (member_id) REFERENCES member (id),
    FOREIGN KEY (book_id) REFERENCES book (id)
);