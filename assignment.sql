-- *************************** Create Database ****************************
CREATE DATABASE IF NOT EXISTS RMS;

-- Now modify Database
USE RMS;

-- Creating Tables
create table Train (No integer not null primary key, Name text not null, Frm text not null, Tu text not null, DTime integer not null, ATime integer not null, Mon integer not null, Tue integer not null, Wed integer not null, Thurs integer not null, Fri integer not null, Sat integer not null, Sun integer not null, Gen integer not null, Sleep integer not null, AC3 integer not null, AC2 integer not null, AC1 integer not null, Running integer not null);
create table Customer (Username varchar(15) not null primary key, Password text not null);
create table Admin (Username varchar(15) not null primary key, Password text not null);
create table Passenger (PNR integer not null primary key, DOJ date not null, Train_no integer not null, Name text not null, Age integer not null, Username text not null, Class integer not null, Reservation_Status integer not null, Cancellation_Status integer not null, Waiting_No integer not null, Berth integer not null);
create table TrainList (No integer not null, Start_Date date not null, Status integer not null, Gen integer not null, Sleep integer not null, AC3 integer not null, AC2 integer not null, AC1 integer not null, WL_Gen integer not null, WL_Sleep integer not null, WL_AC3 integer not null, WL_AC2 integer not null, WL_AC1 integer not null, primary key(No, Start_Date));

-- ************** Applying Relation by applying foriegn key constraint *************************
alter table TrainList add foreign key (No) REFERENCES Train(No) ON DELETE CASCADE;


-- *********************** Inserting values in Tables *****************************

insert into Customer (Username, Password) values ('Shivam', 'Kumar');
insert into Customer (Username, Password) values ('Aman', 'Pawar');
insert into Customer (Username, Password) values ('Kulvendra', 'Singh');

insert into Admin (Username, Password) values ('Shivam', 'Kumar');
insert into Admin (Username, Password) values ('Pawar', 'Aman');
insert into Admin (Username, Password) values ('Singh', 'Kulvendra');

insert into Train values (1, 'Jammu Rajdhani', 'JAT', 'NDLS', 1940, 0500, 1, 0, 1, 0, 1, 1, 1, 10, 11, 5, 4, 2, 1);

insert into Passenger values (1, '2019-05-06', 1, 'Shivam Kumar', 20, 'Shivam', 4, 1, 0, 0, 0);

insert into TrainList values (1, '2019-05-06', 0, 10, 11, 5, 3, 2, 0, 0, 0, 0, 0);