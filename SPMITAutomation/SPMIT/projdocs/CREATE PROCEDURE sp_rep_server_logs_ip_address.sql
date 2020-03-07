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
-- Description:	For the last 7 days, the unique IP addresses that are recorded in the system. 
-- The plotting is in Pie chart, the size denotes the percentage of the total count of the IP over all IPs. 
-- Only those total count greater than 5% of the total circle should be plotted (do not plot the tiny regions).
-- =============================================
ALTER PROCEDURE sp_rep_server_logs_ip_address
AS
BEGIN
SET NOCOUNT ON;
SET XACT_ABORT ON;
	BEGIN TRY	
		DECLARE @StartDate AS DATETIME = CONVERT (datetime,'2019-11-12');

		SELECT	ServerIP_Address,
				ServerIP_Address_Count,
				ServerIP_Address_Count_Percent
		FROM	(	SELECT	ServerIP_Address, 
							COUNT(ServerIP_Address) AS ServerIP_Address_Count,
							COUNT(*) * 100.0 / sum(count(*)) over() AS ServerIP_Address_Count_Percent
					FROM	(	SELECT	ServerIP_Address
								FROM	ServerLogs_Filtered
								WHERE	DATEDIFF(DAY,LogRecorded,@StartDate) <= 5	
							)	ServerLogs_Filtered_By_Days				
					GROUP BY ServerIP_Address
				) TEMP
		WHERE	ServerIP_Address_Count_Percent >= 3
		ORDER BY ServerIP_Address_Count_Percent DESC

	END TRY
	BEGIN CATCH	
		SELECT  'Error||' + (CAST (ERROR_NUMBER() AS NVARCHAR(400))) + '||' + ERROR_MESSAGE() AS ServerLogs
	END CATCH
END
GO
