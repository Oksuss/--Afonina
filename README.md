# --Afonina
# My-pitomnik
1-2.
root@oksana:/home/oks/my_project/.git# cat > pet.txt
Кошка
Собака
Хомяк
root@oksana:/home/oks/my_project/.git# cat > pack_pet.txt
Лошадь
Верблюд
Осёл
root@oksana:/home/oks/my_project/.git# cat pet.txt pack_pet.txt > animals.txt
root@oksana:/home/oks/my_project/.git# cat animals.txt
Кошка
Собака
Хомяк
Лошадь
Верблюд
Осёл
root@oksana:/home/oks/my_project/.git# mv animals.txt humansFriends.txt
root@oksana:/home/oks/my_project/.git# mkdir Dir_for_pets
root@oksana:/home/oks/my_project/.git# mv humansFriends.txt  Dir_for_pets/
root@oksana:/home/oks/my_project/.git# cd  Dir_for_pets/
root@oksana:/home/oks/my_project/.git/Dir_for_pets# ls
humansFriends.txt
3. 
root@oksana:/home/oks/my_project/.git# apt-get install mysql-server
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово
Уже установлен пакет mysql-server самой новой версии (8.0.41-0ubuntu0.24.04.1).
Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 0 пакетов, и 9 пакетов не обновлено.
4. 
root@oksana:/home/oks/my_project/.git# sudo apt-get install cowsay
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово
Предлагаемые пакеты:
  filters cowsay-off
Следующие НОВЫЕ пакеты будут установлены:
  cowsay
Обновлено 0 пакетов, установлено 1 новых пакетов, для удаления отмечено 0 пакетов, и 9 пакетов не обновлено.
Необходимо скачать 18,6 kB архивов.
После данной операции объём занятого дискового пространства возрастёт на 93,2 kB.
Пол:1 http://ru.archive.ubuntu.com/ubuntu noble/universe amd64 cowsay all 3.03+dfsg2-8 [18,6 kB]
Получено 18,6 kB за 1с (24,8 kB/s)
Выбор ранее не выбранного пакета cowsay.
(Чтение базы данных … на данный момент установлено 202905 файлов и каталогов.)
Подготовка к распаковке …/cowsay_3.03+dfsg2-8_all.deb …
Распаковывается cowsay (3.03+dfsg2-8) …
Настраивается пакет cowsay (3.03+dfsg2-8) …
Обрабатываются триггеры для man-db (2.12.0-4build2) …
root@oksana:/home/oks/my_project/.git# cowsay "Привет мир!"
 _____________
< Привет мир! >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
root@oksana:/home/oks/my_project/.git# apt-get remove cowsay
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово
Следующие пакеты будут УДАЛЕНЫ:
  cowsay
Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 1 пакетов, и 9 пакетов не обновлено.
После данной операции объём занятого дискового пространства уменьшится на 93,2 kB.
Хотите продолжить? [Д/н] y
(Чтение базы данных … на данный момент установлено 202965 файлов и каталогов.)
Удаляется cowsay (3.03+dfsg2-8) …
Обрабатываются триггеры для man-db (2.12.0-4build2) …

5. 
  655  rm pet.txt
  656  rm pack_pet.txt
  657  rm animals.txt
  658  ll
  659  cd .git/
  660  cat > pet.txt
  661  cat > pack_pet.txt
  662  cat pet.txt pack_pet.txt > animals.txt
  663  cat animals.txt
  664  ll
  665  mv animals.txt humansFriends.txt
  666  ls
  667  mkdir Dir_for_pets
  668  mv humansFriends.txt  Dir_for_pets/
  669  cd  Dir_for_pets/
  670  ll
  671  git remote add origin https://github.com/Oksuss/--Afonina.git
  672  cd
  673  cd my_project
  674  cd /home/oks/
  675  cd my_project
  676  .git
  677  cd .git/
  678  git add .
  679  git push origin master
  680  echo "# --Afonina" >> README.md
  681  git init
  682  git add README.md
  683  git remote add origin  https://github.com/Oksuss/--Afonina.git
  684  git push -u origin main
  685  git remote add origin https://github.com/Oksuss/--Afonina.git
  686  git branch -M main
  687  git push -u origin main
  688  git remote add origin git@github.com:Oksuss/--Afonina.git
  689  git branch -M main
  690  git push -u origin main
  691  git add README.md
  692  ll
  693  git commit -m "first commit"
  694  git branch -M main
  695  git remote add origin git@github.com:Oksuss/--Afonina.git
  696  git push -u origin main
  697  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
  698  git push -u origin main
  699  cd my_project
  700  cd .git
  701  ll
  702  cd dir_for_pets
  703  cd dir_for_pets/
  704  cd /dir_for_pets
  705  cd Dir_for_pets
  706  ll
  707  cd ..
  708  git push -u origin main
  709  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
  710  git push -u origin main
  711  history
  712  ll
  713  git add .
  714  git remote add origin  https://github.com/Oksuss/--Afonina.git
  715  git push origin master
  716  cd
  717  cd /home/oks/my_project/
  718  ll
  719  cd
  720  mv my_project .git
  721  cd /home/oks/my_project
  722  cd .git
  723  ll
  724  cd ..
  725  ll
  726  cd .git
  727  cd ..
  728  ll
  729  mv --Afonina my_pitomnik
  730  cd --Afonina/
  731  cd Afonina
  732  cd Afonina/
  733  cd /--Afonina/
  734  cd Afonina//
  735  mv --Afonina .git
  736  cd .git
  737  echo "# My-pitomnik" >> README.md
  738  git init
  739  git add README.md;
  740  git commit -m "first commit"
  741  git branch -M main
  742  git remote add origin git@github.com:Oksuss/My-pitomnik.git
  743  git push -u origin main
  744  git remote add origin git@github.com:Oksuss/My-pitomnik.git
  745  git branch -M main
  746  git push -u origin main
  747  ls
  748  cd Dir_for_pets/
  749  ls
  750  cd ..
  751  apt-get update
  752  apt-get install mysql-server
  753  apt-get install clisp
  754  clips
  755  apt-get remove clisp libffcall1b libsigsegv2
  756  sudo apt-get install cowsay
  757  cowsay "Привет мир!"
  758  apt-get remove cowsay
  759  history \> history.txt
  760  history > history.txt
6. root@oksana:/home/oks/my_project/.git# apt install dia
7. mysql> create database humansFriends;
Query OK, 1 row affected (0,04 sec)

mysql> use humansFriends;
Database changed
mysql> create table HPets(
    -> ID INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(30),
    -> type VARCHAR(10),
    -> birthD DATE,
    -> comm TEXT);
Query OK, 0 rows affected (0,26 sec)

mysql> create table pack_pet(
    -> ID INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(30),
    -> type VARCHAR(10),
    -> birthD DATE,
    ->  comm TEXT);
Query OK, 0 rows affected (1,10 sec)
mysql> INSERT INTO HPets (name, type, birthD, comm) VALUES
    -> ('Abby', 'Dog', '2023-03-03', 'Sit, Stay, Voice'),
    -> ('Julia', 'Cat', '2024-04-04', 'Sit, Bring'),
    -> ('Prown', 'Hamster', '2025-05-05', 'Bring, Take'),
    -> ('Moon', 'Dog', '2023-02-02', 'Bring, Stay, Voice'),
    ->  ('Bagle', 'Cat', '2021-01-01', 'Bring, Stay, Take'),
    -> ('Kitty', 'Hamster', '2025-04-02', 'Stay, Take');
Query OK, 6 rows affected (0,16 sec)
Records: 6  Duplicates: 0  Warnings: 0
mysql> INSERT INTO pack_pet (name, type, birthD, comm) VALUES
    -> ('Zizi', 'Horse', '2010-03-11', 'Trot, Canter, Gallop'),
    -> ('Chuk', 'Camel', '2013-11-13', 'Walk, Bring'),
    -> ('Vochy', 'Donkey', '2018-10-18', 'Walk, Take, Go'),
    -> ('Zaza', 'Horse', '2010-05-16', 'Trot, Go, Gallop'),
    -> ('Gek', 'Camel', '2014-10-23', 'Take, Bring'),
    -> ('Bukku', 'Donkey', '2020-05-16', 'Stop, Go');
Query OK, 6 rows affected (0,06 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> DELETE FROM pack_pet WHERE type = 'Camel';
Query OK, 2 rows affected (0,03 sec)

mysql> CREATE TABLE animals AS
    -> select * from HPets
    -> union all
    -> select * from pack_pet;
Query OK, 10 rows affected (0,33 sec)
Records: 10  Duplicates: 0  Warnings: 0
mysql> CREATE TABLE YoungAnimals AS
    -> select
    -> id,
    -> name,
    -> type,
    -> birthD,
    -> comm,
    -> floor(Datediff(curdate(), birthD)/30) as AgeInMonth
    -> from
    -> animals
    -> where
    -> datediff(curdate(), birthD) between 365 and 1095;
Query OK, 3 rows affected (0,24 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> create table allAnimals As
    -> select
    -> 'HPets' as Category,
    -> id,
    -> name,
    -> type,
    -> birthD,
    -> comm
    -> from
    -> HPets
    -> Union all
    -> select
    -> 'pack_pet' as Category,
    -> id,
    -> name,
    -> type,
    -> birthD,
    -> comm
    -> from
    -> pack_pet
    -> union all
    -> select
    -> 'animals' as Category,
    -> id,
    -> name,
    -> type,
    -> birthD,
    -> comm
    -> from
    -> animals
    -> union all
    -> select
    -> 'YoungAnimals' as Category,
    -> id,
    -> name,
    -> type,
    -> birthD,
    -> comm
    -> from
    -> YoungAnimals;
Query OK, 23 rows affected (0,18 sec)
Records: 23  Duplicates: 0  Warnings: 0

