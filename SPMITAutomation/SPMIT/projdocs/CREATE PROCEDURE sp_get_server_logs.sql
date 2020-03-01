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
-- Create date: 03/01/2020
-- Description:	Get Server Logs From Database
-- =============================================
ALTER PROCEDURE sp_get_server_logs (
	@ServerId AS INT)
AS
BEGIN
SET NOCOUNT ON;
SET XACT_ABORT ON;
	BEGIN TRY		
		IF @ServerId IS NULL OR @ServerId <=0 
			THROW 50001, 'ServerId is Mandatory Paramter', 1;
			
		SELECT	Id, ServerLogs 
		FROM	ServerLogs 
		WHERE	ServerID = @ServerId
		ORDER BY Id	

	END TRY
	BEGIN CATCH	
		SELECT  'Error||' + (CAST (ERROR_NUMBER() AS NVARCHAR(400))) + '||' + ERROR_MESSAGE() AS ServerLogs
	END CATCH
END
GO
