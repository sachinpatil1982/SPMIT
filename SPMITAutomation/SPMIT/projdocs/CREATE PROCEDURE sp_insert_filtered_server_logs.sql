-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Sachin Patil
-- Create date: 24/02/2020
-- Description:	Insert Filitered Server Logs in Database
-- =============================================
ALTER PROCEDURE sp_insert_filtered_server_logs( 	
	@ServerId AS INT,
	@UserId as NVARCHAR(400),
	@ServerLogFilePath AS nvarchar(400),
	@IsTransactionSuccessfull int OUTPUT,
	@TransactionMessage nvarchar (800) OUTPUT
) 
AS
BEGIN
SET NOCOUNT ON;
SET XACT_ABORT ON;
	BEGIN TRY
		BEGIN TRANSACTION 
			IF @ServerId IS NULL OR @ServerId <=0 
				THROW 50001, 'ServerId is Mandatory Paramter', 1;

			IF @UserId IS NULL OR @UserId = ''  
				THROW 50002, '@UserId is Mandatory Paramter', 1;

			IF @ServerLogFilePath IS NULL OR @ServerLogFilePath = ''  
				THROW 50003, '@ServerLogFilePath is Mandatory Paramter', 1;
			
			TRUNCATE TABLE ServerLogs_Filtered

			DECLARE @parameters varchar(100)
			CREATE TABLE #tmp (	ServerIP_Address nvarchar(400),
								LogRecorded  nvarchar(400),
								EventSource nvarchar(MAX),
								EventId INT,
								EventCategory INT,
								EventSubSources nvarchar(MAX),
								UserName  nvarchar(400),
								ProjectName  nvarchar(400),
								EventDescriptions nvarchar(MAX))
			DECLARE @fieldsep char(1) = '|';
			DECLARE @recordsep char(1) = char(10);
			DECLARE @sql varchar(8000) = ' 
			BULK INSERT #tmp
				FROM '''+@ServerLogFilePath+'''
				WITH (FIRSTROW = 1, FIELDTERMINATOR = '''+@fieldsep+''', ROWTERMINATOR = '''+@recordsep+''')';

			PRINT (@SQL)
			EXEC (@SQL)

--			BULK INSERT #tmp
--				FROM 'C:\Temp\ServerLogs\results_filtered.txt'
--				WITH (FIRSTROW = 1, FIELDTERMINATOR = '|', ROWTERMINATOR = '
--')
	
			--SELECT * FROM #tmp ORDER BY LogRecorded

			INSERT ServerLogs_Filtered	(	ServerID,
											ServerIP_Address,
											LogRecorded,
											EventSource,
											EventId,
											EventCategory,
											EventSubSources,
											UserName,
											ProjectName,
											EventDescriptions,
											CreatedDate,
											CreatedBy
										) 
									SELECT	TOP 80275 @ServerId AS ServerId,
											ServerIP_Address,
											STUFF((REPLACE((REPLACE((REPLACE(LogRecorded,'[','')),']','')),' +0000','')), PATINDEX('%' + ':' + '%', 
											REPLACE((REPLACE((REPLACE(LogRecorded,'[','')),']','')),' +0000','')), LEN(':'), ' ') AS LogRecorded,
											EventSource,
											EventId,
											EventCategory,
											EventSubSources,
											UserName,
											ProjectName,
											EventDescriptions,											
											GETDATE() AS CreatedDate, 
											@UserId AS CreatedBy
									FROM	#tmp
									ORDER BY LogRecorded
						
			DROP TABLE #tmp

			DELETE FROM ProjectInformation WHERE ServerId = @ServerId

			INSERT INTO ProjectInformation (	ServerId,
												UserName,
												ProjectName,
												CreatedDate,
												CreatedBy)
										SELECT	@ServerId AS ServerId,
												UserName,
												ProjectName,
												GETDATE() AS CreatedDate,
												@UserId AS CreatedBy
										FROM	(	SELECT	DISTINCT UserName, ProjectName 
													FROM	ServerLogs_Filtered 
													WHERE	UserName NOT IN ('users','assets','uploads','admin','dashboard', '''', '-')
															AND (UserName IS NOT NULL OR UserName <> '')
															AND (ProjectName IS NOT NULL OR ProjectName <> '')
															AND ServerId = @ServerId
												) TEMP
										ORDER BY UserName, ProjectName


			SELECT  @IsTransactionSuccessfull=1, @TransactionMessage = 'Successful'

		COMMIT;

	END TRY
	BEGIN CATCH	
		SELECT   @IsTransactionSuccessfull=0, @TransactionMessage = (CAST (ERROR_NUMBER() AS NVARCHAR(400))) + '||' + ERROR_MESSAGE()
		IF @@ERROR <> 0	OR @@TRANCOUNT > 0
			ROLLBACK;
	END CATCH
END
GO
