USE ShoppingDB;
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2),
    Stock INT
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '555-1234'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
(3, 'Alice', 'Johnson', 'alice.johnson@example.com', '555-8765');

INSERT INTO Products (ProductID, ProductName, Price, Stock)
VALUES
(1, 'Laptop', 999.99, 50),
(2, 'Smartphone', 499.99, 100),
(3, 'Tablet', 299.99, 200);

INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES
(1, 1, '2023-07-01'),
(2, 2, '2023-07-02');

INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity)
VALUES
(1, 1, 1, 1),
(2, 1, 3, 2),
(3, 2, 2, 1);

