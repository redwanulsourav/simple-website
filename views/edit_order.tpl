<html>
    <body>
        <form method="POST" action="">
            <p>Product Name: <input name="product_name" value="{{ order.product_name }}"></p>
            <p>Product Price: <input name="product_price" value="{{ order.product_price }}"></p>
            <p>Customer Name: <input name="customer_name" value="{{ order.customer.customer_name }}" readonly> </p>
            <input type="submit">
        </form>
    </body>
</html>