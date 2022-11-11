use Curso
go
create table Alumno(Legajo int primary key not null,
                    Nombre varchar(30)not null,
					Apellido varchar(30) not null,
					Fecha_Nacimiento date not null);
create table Materia(Codigo int primary key not null,
                     Descripcion varchar(50) not null);
create table Cursa(Legajo_Alumno int foreign key references Alumno(Legajo),
                   Codigo_Materia int foreign key references Materia(Codigo));
insert into Alumno values(1,'Sabrina','Benitez','1980-02-23'),
						 (2,'Paola','Perez','1990-05-03'),
						 (3,'Pedro','Paez','1970-07-25'),
						 (4	,'Ana','Rodriguez','2002-07-25'),
						 (5,'Miguel','Suarez','2000-01-21');

insert into Materia values(1,'Quimica'),
						  (2,'Matematica'),
						  (3,'Fisica'),
						  (4,'Literatura'),
						  (5,'Musica');
insert into Cursa values(1,2),
                        (1,5),
						(2,3),
						(1,3),
						(5,1);






				   ;

