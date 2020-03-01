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
TRUNCATE TABLE ServerLogs
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



















