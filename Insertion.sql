
use JOESCHOPS
-- INSERT into Customer values ('Hasini','L',999993999,'abfc@gmail.com','hasini','abcd','bankcolony','Fullerton','CA',92831)

-- INSERT into Employee values ('Chao123','xyz','Wu','Chao','Manager',888888888,'chao@gmail.com')

-- INSERT into Vehicle values (80000000,'Sonic','1234A',1996,'LPW Naturally Aspirated Engines 2, 3 & 4 Cylinder Configurations ',
-- 							'SEL','Car Wash','Seat Adjustment','Average','New', 'Average', 'Average')

-- use JOESCHOPS
-- select * from Customization_Plan

-- insert into Customization_Detail values(80000000,1000,1)

-- insert into Item values(100,1,'paint','paint the car',400.96,150,100,150)

-- insert into Questionnaire values(100,'2022-02-03','How long does it take to complete',null)

-- select Plan_ID from Customization_Detail where Emp_ID=1

-- insert into Customization_Plan values(100,600.29,100,'2022-04-23','2022-08-02',440.16,20.16,600.29-100,'Card','Created','2022-04-23',null)

-- select * from Questionnaire

-- select Item.Plan_ID,Item.Item_ID,Item.Item_name,Item.Item_Desp,Customization_Plan.TE_price,Customization_Plan.Amount_Deposited,Customization_Plan.Estimated_DeliveryDate,Customization_Plan.Amount_due,
-- Customization_Plan.Status from Customization_Plan,Item where Customization_Plan.Plan_ID=100 and Item.Emp_ID=1

-- update Customization_Plan set Estimated_DeliveryDate='2022-09-03',Photo_links='https://hytur' where Plan_ID=100

-- select Question_No,Question_Desp from Questionnaire where Plan_ID=100

-- update Questionnaire set Question_Ans='soon' where Question_No=1 and Plan_ID=100

-- select * from Customization_Detail

-- delete from Customization_Plan where Plan_ID=106
-- delete from Questionnaire where Plan_ID=106
-- delete from Item where Plan_ID=106
-- delete from Customization_Detail where VerificationIN=1002
-- delete from Vehicle where VerificationIN=1002

-- select VerificationIN from Customization_Detail where Emp_ID=5

-- select * from Item 

-- create unique index index_ItemName on Item(Item_name)

-- select Status,Estimated_DeliveryDate,Amount_due,Photo_links,Item.Item_name,Item.Item_Desp from Customization_Plan 
--  inner JOIN Item on Customization_Plan.Plan_ID=106 and Item.Plan_ID=106

--  select * from Customer