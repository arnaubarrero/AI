create table DadesPersonas(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    altura int,
    pes int,
    num_peu int,
    edat int,
    genere int
);

INSERT INTO DadesPersonas (altura, pes, num_peu, edat, genere)
VALUES  ('163','70','37','52','0'), 
        ('172','72','41','21','1'),
        ('168','70','41','24','1'),
        ('180','67','43','22','1');