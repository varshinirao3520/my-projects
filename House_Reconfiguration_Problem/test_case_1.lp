% Test Case 1: Basic reconfiguration
legacyConfig(person(1)).
legacyConfig(person(2)).

legacyConfig(room(3)).
legacyConfig(room(4)).
legacyConfig(roomTOcabinet(3, 5)).
legacyConfig(roomTOcabinet(3, 6)).
legacyConfig(roomTOcabinet(4, 8)).
legacyConfig(roomTOcabinet(4, 9)).

legacyConfig(cabinet(5)).
legacyConfig(cabinet(6)).
legacyConfig(cabinet(8)).
legacyConfig(cabinet(9)).

legacyConfig(cabinetTOthing(5, 11..12)).
legacyConfig(cabinetTOthing(6, 13..14)).
legacyConfig(cabinetTOthing(8, 15..16)).
legacyConfig(cabinetTOthing(9, 17..18)).

legacyConfig(thing(11..18)).
thingShort(11; 12; 15; 16).
thingLong(13; 14; 17; 18).

legacyConfig(personTOthing(1, 11..14)).
legacyConfig(personTOthing(2, 15..18)).
