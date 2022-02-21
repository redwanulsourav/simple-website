<html>
    <body>
        <table>
            <tr>
                <th>
                    Customer Name
                </th>
                <th>
                    Customer Address
                </th>
                <th>
                    Customer Email
                </th>
                <th>
                    Edit customer
                </th>
            </tr>
            
        % for customer in customers:
            <tr>
                <td>
                    <a href = "/view_customer_details/{{customer.customer_name}}"> {{ customer.customer_name }} </a>
                </td>
                <td>
                    {{ customer.customer_address }}
                </td>
                <td>
                    {{ customer.customer_email }}
                </td>
                <td>
                    <a href="/edit_customer/{{ customer.customer_name }}">Edit</a>
                </td>
            </tr>
        </table>
    </body>
</html>