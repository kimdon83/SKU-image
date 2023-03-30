WITH invT as (
    SELECT material, sum(total_stock) as total_stock FROM [ivy.mm.dim.mrp01]
    WHERE total_stock>0
    GROUP BY material
)

SELECT T1.material, T1.ms 
into #msmtrl
FROM [ivy.mm.dim.mtrl] T1
LEFT JOIN sku_image T2 on T1.material=T2.Material
LEFT JOIN invT on T1.material = invT.material
WHERE T1.ms in ('01','03','D1','N1')
and T1.mg <> 'pp'
and T2.Link is null
and invT.material is not null

SELECT ms, count(*) num_mtrl FROM #msmtrl
GROUP BY ms

DROP table #msmtrl


SELECT T1.ms, count(*) num_mtrl FROM sku_image T2
inner JOIN [ivy.mm.dim.mtrl] T1 on T1.material=T2.Material
GROUP BY T1.ms
ORDER BY T1.ms

SELECT * FROM [ivy.mm.dim.mtrl]
where mg ='pp'
