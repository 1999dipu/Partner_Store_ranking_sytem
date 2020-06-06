import React, { Component } from 'react';
import Axios from "axios";
import {withRouter} from 'react-router-dom';

export class Buttons extends Component {        
   
    
    onSubmit=(e)=>{
        e.preventDefault();
        }
   
    nextPath(path) {
        this.props.history.push(path);
      }

      
    render() {
        return (
          <div>
              
              <form align="left" onSubmit={this.onSubmit} >
                  <div>
              </div>
              <div>
                  <table cellSpacing="2" cellPadding="2">
                      <tbody>
                      
                      
                     
                      
                      
                      
                      <tr>
                          <td>
                              <br/>
                              <div style={{color:'Black'}}>
                  <h5><b>Search for a new Amazon Pickup Location</b></h5>
              
              
                              <button type="submit" style={{background: 'orange',borderRadius:'8px'}} onClick={() => this.nextPath('/search') }>
                  Locker's Ranking List
          </button></div>
          <br/>
          <div style={{color:'Black'}}>
                  <h5><b>Onboard a new locker</b></h5>
                              <button type="submit"  style={{background: 'orange',borderRadius:'8px'}} onClick={() => this.nextPath('/onboard') }>
                Onboard Locker Portal
          </button></div>
         
                               <br/><br/>
                          </td>
                          <td colSpan="2">&nbsp;</td>
                      </tr>
                      
                      
                      </tbody>
                  </table>
              </div>

              </form>
              
          </div>
        )
        
    }
}

export default withRouter(Buttons)
