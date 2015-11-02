#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Modules that creates a report"""


def sum_orders(customers, orders):
    """
    This function creates a report with combined dictionary.

    Args:
        customers (dict): name and email
        orders (dict): customer_id and total

    Returns:
        A combined dictionary

    Examples:
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}
    """
    report = {}
    for custo, order_req in customers.iteritems():
        num_orders = 0
        order_count = 0
        for order_req in orders.values():
            if custo in (order_req['customer_id'],):
                num_orders += 1
                order_count += order_req['total']
                report[custo] = {'name': order_req['name'],
                                 'email': order_req['email'],
                                 'orders': num_orders,
                                 'total': order_count,
                                 }
    report = sorted(report.iteritems())
    return report
