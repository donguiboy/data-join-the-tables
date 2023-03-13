# pylint:disable=C0111,C0103
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
datab = conn.cursor()

def detailed_orders(db):#done
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """select OrderID, c.ContactName as Customer,
    e.FirstName as Employee
    from Orders o
    join Customers c on c.CustomerID = o.CustomerID
    join Employees e on e.EmployeeID = o.EmployeeID
    order by OrderID """
    db.execute(query)
    results = db.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """SELECT c.ContactName, round(sum(od.UnitPrice * od.Quantity),2)
    as amount_spent

    FROM OrderDetails od
    JOIN Orders o on o.OrderID  = od.OrderID
    JOIN Customers c on c.CustomerID = o.CustomerID
group by c.ContactName
order by amount_spent ASC
"""
    db.execute(query)
    results = db.fetchall()
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'L
    astName', 6000 (the sum of all purchase)). The order of the information is
    irrelevant'''
    # YOUR CODE HERE
    query="""SELECT e.FirstName, e.LastName, sum(od.UnitPrice * od.Quantity)
    as amount_sold
    FROM Employees e
    join Orders o on e.EmployeeID = o.EmployeeID
    JOIN OrderDetails od on o.OrderID = od.OrderID
    GROUP BY FirstName,LastName
    ORDER BY amount_sold DESC
    """
    db.execute(query)
    results = db.fetchone()
    return results
    #otra forma results = db.fetchall()
    #for i in results:
    #    return i

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query="""SELECT c.ContactName, count(DISTINCT  o.OrderID) as number_of_orders
FROM  Customers c
left join  Orders o on o.CustomerID = c.CustomerID
left join OrderDetails od on o.OrderID = od.OrderID
group by c.CustomerID
order by number_of_orders
"""
    db.execute(query)
    results = db.fetchall()
    return results
