<html>
    <head>
    </head>
    <body>
        <table>
            <tr>
                <th>
                    Product Name
                </th>
                <th>
                    Customer Name
                </th>
                <th>
                    Customer Email
                </th>
                <th>
                    Product Price
                </th>
            </tr>
            % for order in orders:
            <tr>
                <td>
                    {{ order.product_name }}
                </td>
                <td>
                    {{ order.customer.customer_name }}
                </td>
                <td>
                    {{ order.customer.customer_email }}
                </td>
                <td>
                    {{ order.product_price }}
                </td>
                <td>
                    <a href="/edit_order/{{ order.product_name }}/{{ order.customer.customer_name }}/{{ order.product_price }}"> Edit </a>
                </td>
                <td>
                    <a href="/delete_order/{{ order.product_name }}/{{ order.customer.customer_name }}/{{ order.product_price }}"> Delete </a>
                </td>
            </tr>
        </table>
    </body>

</html>