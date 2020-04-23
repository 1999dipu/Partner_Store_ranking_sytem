import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Header from "./layout/Header";
import Dashboard from "./leads/Dashboard";
import { Provider } from "react-redux";
import store from "../store";
import Form from "./leads/Form";
class App extends Component {
  searchbyaddress=(address) =>{
    console.log(address)
  }
  searchbyzip=(zip) =>{
    console.log(zip)
  }
  searchbylandmark=(landmark) =>{
    console.log(landmark)
  }
  searchbylockername=(lockername) =>{
    console.log(lockername)
  }
  queryby=(query) =>{
    
    console.log(query)
  }
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          

          <div className="container">
            <Form 
            searchbyaddress={this.searchbyaddress}
            searchbyzip={this.searchbyzip}
            searchbylandmark={this.searchbylandmark}
            searchbylockername={this.searchbylockername}
            queryby={this.queryby}
            />
            
            
          </div>
        </Fragment>

      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
