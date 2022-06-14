import React from 'react';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import LoginForm from "./components/login_form/login_form";
import BaseTemplate from "./components/base_template/base_template";
import AuctionsList from "./components/auctions_list/AuctionsList";
import AuctionCreator from "./components/auction_creator/AuctionCreator";

class RouterApp extends React.Component{
    render(){
        return(
            <Router>
                <Routes>
                    <Route path="/login" element={<LoginForm />} />
                    <Route path="/app" element={<BaseTemplate />} >
                        <Route path="list" element={<AuctionsList />} />
                        <Route path="create" element={<AuctionCreator />} />
                    </Route>
                </Routes>
            </Router>
        )
    }
}

export default RouterApp;