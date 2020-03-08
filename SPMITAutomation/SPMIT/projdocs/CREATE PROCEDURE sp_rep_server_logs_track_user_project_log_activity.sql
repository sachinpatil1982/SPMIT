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
-- Description:	Continue with the plotting in item 2: when click the section, 
-- it should plot a bar graph, which plots for this user, across the last 30 days, 
-- the total count of code upload on each day. 
-- In the plot, it should also show the total number of unique project that the user upload on this day.
-- =============================================
CREATE PROCEDURE sp_rep_server_logs_track_user_project_log_activity (
	@ServerId AS INT,
	@UserName AS NVARCHAR(400)
)
AS
BEGIN
SET NOCOUNT ON;
SET XACT_ABORT ON;
	BEGIN TRY	
		DECLARE @StartDate AS DATETIME = CONVERT (datetime,'2019-11-12');

		SELECT	UserName,
				ProjectName,
				LogRecorded,
				Log_Count
		FROM	(	SELECT	UserName,
							ProjectName,
							LogRecorded,
							COUNT(LogRecorded) AS Log_Count							
					FROM	(	SELECT	SLF.ServerIP_Address,
										CONVERT(DATE, SLF.LogRecorded) AS LogRecorded,
										SLF.EventSource,
										SLF.EventSubSources,
										SLF.EventDescriptions,
										DATEDIFF(DAY,SLF.LogRecorded,@StartDate) AS DaysDifference,
										PJI.UserName,
										PJI.ProjectName 
								FROM	ServerLogs_Filtered SLF
										INNER JOIN ProjectInformation PJI ON PJI.ServerId = SLF.ServerId AND PJI.UserName = SLF.UserName AND PJI.ProjectName = SLF.ProjectName
								WHERE	DATEDIFF(DAY,SLF.LogRecorded,@StartDate) <= 30
										AND PJI.ServerId  = @ServerId
										AND PJI.UserName = @UserName
							)	UserLogs_Filtered_By_Days				
					GROUP BY UserName,ProjectName,LogRecorded
				) TEMP		
		ORDER BY LogRecorded, ProjectName

	END TRY
	BEGIN CATCH	
		SELECT  'Error||' + (CAST (ERROR_NUMBER() AS NVARCHAR(400))) + '||' + ERROR_MESSAGE() AS ServerLogs
	END CATCH
END
GO
