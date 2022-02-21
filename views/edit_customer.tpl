<html>
    <body>
        <h1> {{ customer.customer_name }} </h1>
        <form method = "POST" action="">
            <input name="customer_address" value="{{ customer.customer_address }}"> <br>
            <input name="customer_email" value="{{ customer.customer_email }}"> <br>
            <input type="submit">
        </form>
    </body>
</html>