import  React, { Component } from  'react';

import  OrderService  from  './OrderService';

const  orderService  =  new  OrderService();


class  OrderList  extends  Component {

	constructor(props) {
		super(props);
		this.state  = {
			orders: [],
		};
	}


    componentDidMount() {
        var  self  =  this;
        orderService.getOrders().then(function (result) {
            self.setState({ orders: result})
        });
    }

    render() {

        return (
            <div  className="order--list">
                <table  className="table">
                <thead  key="thead">
                <tr>
                    <th>#</th>
                    <th>order_number</th>
                    <th>price_in_usd</th>
                    <th>delivery_date</th>
                    <th>price_in_rub</th>
                </tr>
                </thead>
                <tbody>
                {this.state.orders.map(c  =>
                    <tr  key={c.id}>
                    <td>{c.id}</td>  
                    <td>{c.order_number}</td>
                    <td>{c.price_in_usd}</td>
                    <td>{c.delivery_date}</td>
                    <td>{c.price_in_rub}</td>
                </tr>)}
                </tbody>
                </table>
            </div>
            );
      }
}

export  default  OrderList;