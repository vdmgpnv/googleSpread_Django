import  React, { Component } from  'react';
import { BrowserRouter, Routes } from  'react-router-dom'
import { Route, Link } from  'react-router-dom'
import  OrderList  from  './OrderList'
import  './App.css';


const BaseLayout = () => (
  <div className="container-fluid">
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  Test task
</nav>  

    <div className="content">
      <Routes>
      <Route path="/"  element={<OrderList/>} exact />
      </Routes>
      
    </div>

  </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;