INSERT INTO Исполнитель (Псевдоним)
VALUES ('Linkin park'), ('One Republic'),
('Loqiemean'), ('Луи Армстронг'),
('Rammstein'), ('Тимы Белорусских');

INSERT INTO Жанр (Название)
VALUES ('Рок'), ('Электронная музыка'),
('Джаз'), ('Индастриал-метал'),
('Хард-рок'), ('хип-хоп'),
('синтипоп');

INSERT INTO Жанр_Исполнитель (Исполнитель_id, Жанр_id)
VALUES (1, 1), (2, 1), (3, 2), (4, 3), (5, 4),  (5, 5),  (6, 6), (6, 7);

INSERT INTO Альбом (Название, Год_выпуска, Количество_Треков)
VALUES ('One More Light', '2017-02-16', 10), ('Oh My My', '2016-10-07', 16),
('Rammstein', '2019-05-17', 11), ('Твой первый диск — моя кассета', '2019-01-30', 7);

INSERT INTO Исполнитель_Альбом (Альбом_id, Исполнитель_id)
VALUES (1, 1), (2, 2), (3, 5), (4, 6);

INSERT INTO Трек (Название, Длительность, Альбом_id)
VALUES ('Let’s Hurt Tonight', 194, 2), ('Future Looks Good', 211, 2), ('Oh My My', 219, 2), ('Kids', 239, 2), 
('Dream', 213, 2), ('Choke', 228, 2), ('A.I.', 310, 2), ('Better', 207, 2),
('Born', 266, 2), ('Fingertips', 256, 2), ('Human', 221, 2), ('Lift Me Up', 226, 2),
('NbHD', 224, 2), ('Wherever I Go', 230, 2), ('All These Things', 199, 2), ('Heaven', 259, 2),
('Nobody Can Save Me', 224, 1), ('Good Goodbye', 211, 1), ('Talking to Myself', 231, 1), ('Battle Symphony', 216, 1),
('Invisible', 214, 1), ('Heavy', 169, 1), ('Sorry for Now', 203, 1), ('Halfway Righ', 219, 1),
('One More Light', 255, 1), ('Sharp Edges', 178, 1), ('Deutschland', 323, 3), ('Radio', 277, 3),
('Zeig dich', 255, 3), ('Ausländer', 231, 3), ('Sex', 236, 3), ('Puppe', 273, 3),
('Was ich liebe', 269, 3), ('Diamant', 154, 3), ('Weit weg', 260, 3), ('Tattoo', 251, 3),
('Hallomann', 251, 3), ('Я больше не напишу', 191, 4), ('Витаминка', 176, 4), ('Возвращаться уже поздно', 199, 4),
('Цветочный сад', 181, 4), ('Руферы', 191, 4), ('Мальчик бабл-гам', 180, 4), ('Песня-SOS', 215, 4);

INSERT INTO Сборник (Название, Год_выпуска)
VALUES ('100 лучших песен 2019-го', '2019-10-01');

INSERT INTO Состав_сборника (Трек_id, Сборник_id)
VALUES (39, 1), (27, 1);