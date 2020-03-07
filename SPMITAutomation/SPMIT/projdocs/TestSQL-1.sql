SELECT * FROM SystemLogs order by  Id DESC
--TRUNCATE TABLE SystemLogs
--INSERT INTO SystemLogs (ServerId, UserId, ModuleName, LogLevel, LogLevelName, LogMessage, CreatedDate, CreatedBy) 
--VALUES (1, 'SachinPatil', 'Infrastructure_File_Managment.Py', '10', 'DEBUG', 
--'Method modified input parameter - Input String Modified - Test Data', 
--(convert(datetime, '20-02-16 18:05:32')), 'SachinPatil')

--INSERT INTO SystemLogs (ServerId, UserId, ModuleName, LogLevel, LogLevelName, LogMessage, CreatedDate, CreatedBy) 
--SELECT 1, 'SachinPatil', 'Infrastructure_File_Managment.Py', '10', 'DEBUG', 
--'Method modified input parameter - Input String Modified - Test Data', 
--(convert(datetime, '20-02-16 18:05:32')), 'SachinPatil'

--SELECT CONVERT(datetime, '20-02-16 18:05:32', 131)

--SELECT * FROM ServerDetails
--INSERT INTO ServerDetails 
--SELECT 'Test Server','Test Server', 1, GETDATE(), 'SachinPatil'
SELECT * FROM ServerLogs
SELECT * FROM ServerLogs WHERE ServerLogs LIKE '%- abc-ay%'
SELECT COUNT(*) FROM ServerLogs
--TRUNCATE TABLE ServerLogs
SELECT getdate()
sp_who
kill 61
DECLARE @ServerId AS INT = 1;
DECLARE	@UserId as NVARCHAR(400) = 'SachinPatil'
DECLARE	@ServerLogFilePath AS nvarchar(400) = 'C:\Temp\ServerLogs\results.txt';
DECLARE @IsTransactionSuccessfull int;
DECLARE @TransactionMessage nvarchar (800);
EXECUTE sp_insert_server_logs @ServerId, @UserId, @ServerLogFilePath, @IsTransactionSuccessfull OUTPUT, @TransactionMessage OUTPUT
SELECT @IsTransactionSuccessfull, @TransactionMessage

EXECUTE sp_get_server_logs 1
--35100||Error number 10000 in the THROW statement is outside the valid range. 
--Specify an error number in the valid range of 50000 to 2147483647.
--Transaction count after EXECUTE indicates a mismatching number of BEGIN and COMMIT statements. Previous count = 0, current count = 1.

SELECT * FROM ServerLogs_Filtered
SELECT COUNT(*) FROM ServerLogs_Filtered
TRUNCATE TABLE ServerLogs_Filtered

DECLARE @ServerId AS INT = 1;
DECLARE	@UserId as NVARCHAR(400) = 'SachinPatil'
DECLARE	@ServerLogFilePath AS nvarchar(400) = 'C:\Temp\ServerLogs\results_filtered.txt';
DECLARE @IsTransactionSuccessfull int;
DECLARE @TransactionMessage nvarchar (800);
EXECUTE sp_insert_filtered_server_logs @ServerId, @UserId, @ServerLogFilePath, @IsTransactionSuccessfull OUTPUT, @TransactionMessage OUTPUT
SELECT @IsTransactionSuccessfull, @TransactionMessage

SELECT CONVERT(datetime, '13/Oct/2019 03:06:09 +0000', 126)

241||Conversion failed when converting date and/or time from character string.

SELECT STUFF('13/Oct/2019:03:06:09 +0000', CHARINDEX(':', '13/Oct/2019:03:06:09 +0000'), LEN(':'), '')
select STUFF('13/Oct/2019:03:06:09 +0000', PATINDEX('%' + ':' + '%', '13/Oct/2019:03:06:09 +0000'), LEN(':'), ' ')
7330||Cannot fetch a row from OLE DB provider "BULK" for linked server "(null)".

SELECT * FROM [dbo].[ServerLogs_IP_Address] ORDER BY ServerIP_Address_Count_Percent DESC
EXECUTE sp_rep_server_logs_ip_address

SELECT TOP 1 * FROM ServerLogs_Filtered ORDER BY LogRecorded DESC
2019-11-12 11:25:48.000
SELECT CONVERT (datetime,'2020-03-07')
SELECT DATEDIFF(DD, '2017/08/25 07:00', '2017/08/28 12:45') AS DateDiff; 

DECLARE @StartDate AS DATETIME = CONVERT (datetime,'2019-11-12');
SELECT	ServerIP_Address,LogRecorded,DATEDIFF(DAY,LogRecorded,@StartDate)
FROM	ServerLogs_Filtered
WHERE	DATEDIFF(DAY,LogRecorded,@StartDate) <= 5





