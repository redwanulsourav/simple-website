<html>
    <body>
        <table>
            % for order in orders:
            <tr>
                <td>
                    {{ order.product_name }}
                </td>
    
                <td>
                    {{ order.product_price }}
                </td>
            </tr>
        </table>
    </body>
</html>