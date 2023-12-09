--Query 1
/*
Count the number of ships that are afiliated with "khanid kingdom"
and have a weapon specialist and a ship equipped with at least a
caliber 3 weapon. 
*/
SELECT COUNT(DISTINCT ships.ship_id)
FROM ships JOIN militarypersons ON ships.ship_id = militarypersons.ship_id
JOIN weaponmodules ON ships.ship_id = weaponmodules.ship_id
WHERE ships.affiliation = 'khanid kingdom'
  AND militarypersons.specialization = 'weapons'
  AND weaponmodules.caliber >= 3;

--Query 2
/*
Gives ships ids, type and their galaxy for ships that are afiliated
with "caldari" and have a weapon of caliber at least 2, shield of size 
at least 2, an energy module with an output of less than 80 and an at least 3
engineers. 
*/
SELECT ships.ship_id, ships.type, galaxies.name
FROM ships JOIN militarypersons ON ships.ship_id = militarypersons.ship_id
JOIN weaponmodules ON ships.ship_id = weaponmodules.ship_id
JOIN shieldmodules ON ships.ship_id = shieldmodules.ship_id
JOIN energymodules ON ships.ship_id = energymodules.ship_id
JOIN galaxies ON ships.galaxy_id = galaxies.galaxy_id
WHERE ships.affiliation = 'caldari'
  AND weaponmodules.caliber >= 2
  AND shieldmodules.size >= 2
  AND energymodules.output < 80
GROUP BY ships.ship_id,galaxies.galaxy_id
HAVING COUNT(DISTINCT CASE WHEN militarypersons.specialization = 'engineer' THEN militarypersons.military_id END) >= 3;

--Query 3
/*
Add an engineer on a mother ship
*/
INSERT INTO militarypersons (military_id, name, age, rank, specialization, ship_id)
VALUES ((SELECT MAX(military_id) + 1 FROM militarypersons), 'Query McGuyer', 25, 3, 'engineer',122);

--Query 4
/*
Delete the last added crew member
*/
DELETE FROM militarypersons
WHERE military_id IN (SELECT MAX(military_id) FROM militarypersons);
SELECT MAX(military_id) FROM militarypersons;