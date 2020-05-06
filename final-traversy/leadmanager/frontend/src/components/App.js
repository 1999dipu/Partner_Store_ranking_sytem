import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Form from "./leads/Form";
import LockersList from './LockersList';
import {BrowserRouter as Router,Switch,Route} from "react-router-dom";
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
      <Router>
        <Fragment>
          <div className="container">
            <Form 
            searchbyaddress={this.searchbyaddress}
            searchbyzip={this.searchbyzip}
            searchbylandmark={this.searchbylandmark}
            searchbylockername={this.searchbylockername}
            queryby={this.queryby}
            />
            
            <LockersList/>

            <Route path="listview/" render={
              ()=>{
                return <h1>List View is here</h1>;
              }
            }
            />
          </div>
        </Fragment>
      </Router>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
