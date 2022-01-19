AS (
	SELECT TOP (65536) ()
	FROM [master].[sys].[columns] col
	CROSS JOIN [master].[sys].[objects] obj
	), chars
AS (
	SELECT nums.[CodePoint], CONVERT(VARCHAR(4), NCHAR(nums.[CodePoint]) COLLATE Latin1_General_100_CI_AS_SC_UTF8)
	FROM nums
	
	UNION ALL
	
	SELECT tmp.val, CONVERT(VARCHAR(4), CONVERT(NVARCHAR(5), tmp.hex) COLLATE Latin1_General_100_CI_AS_SC_UTF8)
	FROM (
		VALUES (65536, 0x00D800DC), -- Linear B Syllable B008 A (U+10000)
			(67618, 0x02D822DC), -- Cypriot Syllable Pu (U+10822)
			(129384, 0x3ED868DD) -- Pretzel (U+1F968)
		) tmp(val, hex)
	)
SELECT chr.[CodePoint], COALESCE(chr.[TheChar], N'TOTALS:') AS [Character], chr.[UTF8] AS [UTF8_Hex]
	---
	CONVERT(VARBINARY(4), CONVERT(NVARCHAR(3), chr.[TheChar])) AS [UTF16(LE)_Hex]
	---
	((DATALENGTH(CONVERT(NVARCHAR(3), chr.[TheChar]))) - (DATALENGTH(chr.[TheChar])))
FROM chars chr
GROUP BY ROLLUP((chr.[CodePoint], chr.[TheChar], chr.[UTF8]));

