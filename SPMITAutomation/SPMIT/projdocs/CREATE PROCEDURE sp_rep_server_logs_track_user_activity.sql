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
-- Description:	For the last 30 days, the users that are active. 
-- “Active” means that user should upload the code at least three times per month. 
-- Use Pie chart to plot this. Only those total count greater than 5% of the total circle should be plotted 
-- (do not plot the tiny regions).
-- =============================================
ALTER PROCEDURE sp_rep_server_logs_track_user_activity (
	@ServerId AS INT
)
AS
BEGIN
SET NOCOUNT ON;
SET XACT_ABORT ON;
	BEGIN TRY	
		DECLARE @StartDate AS DATETIME = CONVERT (datetime,'2019-11-12');

		SELECT	UserName,
				User_Count,
				User_Count_Percent
		FROM	(	SELECT	UserName, 
							COUNT(UserName) AS User_Count,
							COUNT(*) * 100.0 / sum(count(*)) over() AS User_Count_Percent
					FROM	(	SELECT	SLF.ServerIP_Address,
										SLF.LogRecorded,
										SLF.EventSource,
										SLF.EventSubSources,
										SLF.EventDescriptions,
										DATEDIFF(DAY,SLF.LogRecorded,@StartDate) AS DaysDifference,
										PJI.UserName,
										PJI.ProjectName 
								FROM	ServerLogs_Filtered SLF
										INNER JOIN ProjectInformation PJI ON PJI.ServerId = SLF.ServerId AND PJI.UserName = SLF.UserName AND PJI.ProjectName = SLF.ProjectName
								WHERE	DATEDIFF(DAY,LogRecorded,@StartDate) <= 30
										AND PJI.ServerId  = @ServerId
							)	UserLogs_Filtered_By_Days				
					GROUP BY UserName
				) TEMP
		WHERE	User_Count_Percent >= 1
		ORDER BY User_Count_Percent DESC

	END TRY
	BEGIN CATCH	
		SELECT  'Error||' + (CAST (ERROR_NUMBER() AS NVARCHAR(400))) + '||' + ERROR_MESSAGE() AS ServerLogs
	END CATCH
END
GO
