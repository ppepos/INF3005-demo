drop table personne;

create table personne (
  id integer primary key,
  nom varchar(50),
  prenom varchar(25),
  age integer
);

insert into personne values (0, "Paul", "Houde", 51);
