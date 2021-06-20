CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN
SET
    N = N -1;

RETURN (
    SELECT
        DISTINCT e.Salary
    from
        Employee e
    ORDER BY
        Salary DESC
    LIMIT
        N, 1
);

END