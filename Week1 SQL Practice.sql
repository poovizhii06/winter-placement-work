-- Week 1 SQL Practice

CREATE TABLE student (
    id INT,
    name VARCHAR(50),
    age INT
);

INSERT INTO student VALUES (1, 'Arun', 20);
INSERT INTO student VALUES (2, 'Meena', 21);

SELECT * FROM student;
SELECT * FROM student WHERE age > 20;
