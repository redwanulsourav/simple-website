<html>
    <head>
        <title>
            Add a new order
        </title>
    </head>
    
    <body>
        <form action = "/add_order" method="POST">
            <p>Product Name: <input type="text" name="product_name"></p>
            <p>Customer Name: <input type="text" name="customer_name"></p>
            <p>Price: <input type="text" name="product_price"></p>
            <input type = "submit">
        </form>
    </body>
</html>