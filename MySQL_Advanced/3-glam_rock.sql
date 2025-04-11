-- Get band name and their lifespan in years for Glam rock bands
SELECT band_name,
	COALESCE((IFNULL(split, 2024)) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';