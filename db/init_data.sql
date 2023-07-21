TRUNCATE TABLE status CASCADE;

TRUNCATE TABLE member RESTART IDENTITY CASCADE;

TRUNCATE TABLE book RESTART IDENTITY CASCADE;

TRUNCATE TABLE author RESTART IDENTITY CASCADE;

INSERT INTO member VALUES (default,'Jose');
INSERT INTO member VALUES (default,'Jaime');
INSERT INTO member VALUES (default,'Akansha');

INSERT INTO author VALUES (default, 'Vitalii', 'Silii', '1989-12-05');
INSERT INTO author VALUES (default, 'Thomas', 'Mcguane', '1960-04-30');
INSERT INTO author VALUES (default, 'Neil', 'Gaiman', '1970-08-15');

INSERT INTO book VALUES (default, 1, 'Wings of the fire', NULL, 'Self help');
INSERT INTO book VALUES (default, 1, 'Into the void', NULL, 'Horror');

INSERT INTO book VALUES (default, 2, 'The longest night', 'Its about fishing...', 'Short stories');
INSERT INTO book VALUES (default, 2, 'The biggest trout', NULL, 'Testimonial');
INSERT INTO book VALUES (default, 2, 'Hooking Tarpon', NULL, 'Short stories');

INSERT INTO book VALUES (default, 3, 'Norse Mythology', 'Valhalla comes', 'Mythology');
INSERT INTO book VALUES (default, 3, 'American gods', 'Trippy take on theology', 'Theology');

INSERT INTO status VALUES (1, 1, 'reading', 20, '2022-06-21', NULL);
INSERT INTO status VALUES (2, 1, 'reading', 50, '2023-05-01', NULL);
INSERT INTO status VALUES (3, 1, 'complete', 100, '2023-05-01', '2023-06-01');

INSERT INTO status VALUES (1, 2, default, default, NULL, NULL);
INSERT INTO status VALUES (2, 2, 'reading', 40, '2023-01-01', NULL);
INSERT INTO status VALUES (3, 2, 'complete', 100, '2023-01-10', '2023-05-15');

INSERT INTO status VALUES (1, 3, default, default, NULL, NULL);
INSERT INTO status VALUES (2, 3, 'pending', 20, '2022-05-19', NULL);
INSERT INTO status VALUES (3, 3, 'complete', 100, '2022-06-20', '2023-01-25');