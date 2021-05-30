SELECT
    Name AS Customers
FROM
    Customers c
    LEFT JOIN Orders o ON c.Id = o.customerId
WHERE
    o.Id IS NULL