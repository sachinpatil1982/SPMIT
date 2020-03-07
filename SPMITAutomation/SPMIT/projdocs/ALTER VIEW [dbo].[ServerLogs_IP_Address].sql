USE [SPMIT]
GO

/****** Object:  View [dbo].[ServerLogs_IP_Address]    Script Date: 3/7/2020 4:18:34 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

ALTER VIEW [dbo].[ServerLogs_IP_Address]
AS
SELECT	ServerIP_Address, 
		COUNT(ServerIP_Address) AS ServerIP_Address_Count,
		COUNT(*) * 100.0 / sum(count(*)) over() AS ServerIP_Address_Count_Percent
FROM	dbo.ServerLogs_Filtered
GROUP BY ServerIP_Address

GO


