import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';


export default class OrderService{

    constructor(){}

    getOrders() {
		const url = `${API_URL}/api/v1/get_order_data/`;
		return axios.get(url).then(response => response.data);
	}  


}