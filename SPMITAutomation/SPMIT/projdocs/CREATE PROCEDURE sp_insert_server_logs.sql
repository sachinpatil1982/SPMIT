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
-- Description:	Insert Server Logs in Database
-- =============================================
ALTER PROCEDURE sp_insert_server_logs( 	
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
			
			TRUNCATE TABLE ServerLogs

			DECLARE @parameters varchar(100)
			CREATE TABLE #tmp (ServerLogs NVARCHAR(MAX))
			DECLARE @fieldsep char(1) = ',';
			DECLARE @recordsep char(1) = char(10);
			DECLARE @sql varchar(8000) = ' 
			BULK INSERT #tmp
				FROM '''+@ServerLogFilePath+'''
				WITH (FIRSTROW = 1, ROWTERMINATOR = '''+@recordsep+''')';
			
			EXEC (@SQL)
	
			--SELECT * FROM #tmp

			INSERT ServerLogs	(	ServerID,
									ServerLogs,
									CreatedDate,
									CreatedBy
								) 
							SELECT	@ServerId AS ServerId,
									REPLACE(ServerLogs,'- abc-ay','- -') AS ServerLogs,
									GETDATE() AS CreatedDate, 
									@UserId AS CreatedBy
							FROM	#tmp
						
			DROP TABLE #tmp

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
