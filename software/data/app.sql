create table DadesPersonas(
    id      int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    altura  int NOT NULL,
    pes     int NOT NULL,
    num_peu int NOT NULL,
    edat    int NOT NULL,
    genere  int NOT NULL
);

INSERT INTO DadesPersonas (altura, pes, num_peu, edat, genere)
VALUES  (158, 55, 36, 28, 0),
        (165, 60, 38, 34, 0),
        (170, 68, 40, 40, 0),
        (175, 75, 42, 35, 1),
        (182, 85, 44, 50, 1),
        (160, 52, 35, 22, 0),
        (178, 78, 43, 29, 1),
        (155, 50, 34, 30, 0),
        (185, 90, 45, 45, 1),
        (167, 65, 39, 27, 0),
        (172, 77, 41, 38, 1),
        (159, 54, 36, 25, 0),
        (176, 72, 42, 33, 1),
        (162, 59, 37, 31, 0),
        (180, 80, 43, 40, 1);