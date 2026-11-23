CREATE TABLE "public".aircrafts(
aircraft_code CHAR(3) NOT NULL,
model TEXT NOT NULL,
range INTEGER NOT NULL,
CHECK(range > 0),
PRIMARY KEY (aircraft_code)
);

INSERT INTO "public".aircrafts(aircraft_code, model, range) values
('773', 'Boeing 777-300', 11100),
('763', 'Boeing 767-300', 7900),
('733', 'Boeing 737-300', 4200),
('320', 'Airbus A320-200', 5700),
('321', 'Airbus A321-200', 5600),
('319', 'Airbus A319-100', 6700),
('CN1', 'Cessna 208 Caravan', 1200),
('CR2', 'Bombardier CRJ-200', 2700);

SELECT * FROM "public".aircrafts;

SELECT model, aircraft_code, range
FROM "public".aircrafts
ORDER BY model

SELECT model, aircraft_code, range
FROM "public".aircrafts
WHERE range >= 4000 AND range <=6000;

UPDATE "public".aircrafts SET range = 3500
WHERE aircraft_code = 'SU9';

SELECT * FROM "public".aircrafts
WHERE aircraft_code = 'SU9';

DELETE FROM "public".aircrafts
WHERE aircraft_code = 'CN1';

CREATE TABLE "public".seats(
aircraft_code CHAR(3) NOT NULL,
seat_no VARCHAR(4) NOT NULL,
fare_conditions VARCHAR(10) NOT NULL,
CHECK
(fare_conditions IN ('Economy', 'Comfort', 'Business')
),
PRIMARY KEY (aircraft_code, seat_no),
FOREIGN KEY (aircraft_code)
REFERENCES "public".aircrafts (aircraft_code)
ON DELETE CASCADE
);

INSERT INTO "public".seats values
('CR2', '1A', 'Business');
('CR2', '1B', 'Business');
('CR2', '10A', 'Economy');
('CR2', '10B', 'Economy');
('CR2', '1OF', 'Economy');
('CR2', '20F', 'Economy');

SELECT aircraft_code, count(*) From "public".seats
GROUP BY aircraft_code

SELECT aircraft_code, count(*) FROM "public".orders
GROUP BY aircraft_code
ORDER BY count