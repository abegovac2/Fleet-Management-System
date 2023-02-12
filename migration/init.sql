CREATE TABLE IF NOT EXISTS vehicle (
    id SERIAL PRIMARY KEY,
    type varchar(50),
    registration varchar(50)
);

CREATE TABLE IF NOT EXISTS driver (
    id SERIAL PRIMARY KEY,
    full_name varchar(100),
    points int
);

CREATE TABLE IF NOT EXISTS trip (
    id SERIAL PRIMARY KEY,
    departure_geo_point varchar(100),
    destination_geo_point varchar(100)
);

CREATE TABLE IF NOT EXISTS vehicle_drivers(
    vehicle_id int,
    driver_id int,
    CONSTRAINT fk_vehicle_id
        FOREIGN KEY(vehicle_id)
        REFERENCES vehicle
        ON DELETE CASCADE,
    CONSTRAINT fk_driver_id
        FOREIGN KEY(driver_id)
        REFERENCES driver
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS vehicle_trip(
    vehicle_id int,
    trip_id int,
    CONSTRAINT fk_vehicle_id
        FOREIGN KEY(vehicle_id)
        REFERENCES vehicle
        ON DELETE CASCADE,
    CONSTRAINT fk_trip_id
        FOREIGN KEY(trip_id)
        REFERENCES trip
        ON DELETE CASCADE
);
