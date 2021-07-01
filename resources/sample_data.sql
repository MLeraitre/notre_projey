INSERT INTO people (first_name, last_name, birthday, sex, mass) VALUES ('Pierre', '', '2000-04-01', 'male', 70);
INSERT INTO people (first_name, last_name, birthday, sex, mass) VALUES ('Marie', '', '2000-08-01', 'female', 50);
INSERT INTO people (first_name, last_name, birthday, sex, mass) VALUES ('Alex', '', '2000-12-01', 'male', 65);

INSERT INTO beverage (beverage_name, alcohol_proportion, beverage_type) VALUES ('Goudale', 0.07, 'beer');
INSERT INTO beverage (beverage_name, alcohol_proportion, beverage_type) VALUES ('Poliakov', 0.4, 'vodka');
INSERT INTO beverage (beverage_name, alcohol_proportion, beverage_type) VALUES ('Graves', 0.13, 'wine');

INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (1, 2, '2020-06-01 22:00:00', 'Marie s apartment', 0.01);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (2, 3, '2020-06-01 22:05:00', 'Marie s apartment', 0.15);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (3, 1, '2020-06-01 22:00:00', 'Marie s apartment', 0.33);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (3, 1, '2020-06-01 22:15:00', 'Marie s apartment', 0.33);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (1, 3, '2020-06-15 20:00:00', 'Pierre s apartment', 0.15);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (1, 1, '2020-06-30 18:00:00', 'Bar', 0.25);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (2, 1, '2020-06-30 18:00:00', 'Bar', 0.5);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (3, 3, '2020-06-30 18:00:00', 'Bar', 0.55);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (2, 2, '2020-06-30 18:30:00', 'Bar', 0.01);
INSERT INTO drink (id_people, id_beverage, drink_date, place, volume) VALUES (3, 2, '2020-06-30 18:30:00', 'Bar', 0.01);
