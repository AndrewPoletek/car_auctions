import React from 'react';
import {Layout, Menu} from "antd";
import {Outlet, Link} from "react-router-dom";

const { Header, Footer, Sider, Content } = Layout;

const BaseTemplate = () =>{
    return(
            <Layout>
                <Header className="header">
                    <h1 style={{color:"white"}}>Car Auctions System</h1>
                </Header>
                <Layout>
                    <Sider>
                        <Menu theme="dark" mode="vertical" defaultSelectedKeys>
                            <Menu.Item><Link to="create">Utwórz Aukcje</Link></Menu.Item>
                            <Menu.Item><Link to="list">Lista aukcji</Link></Menu.Item>
                            <Menu.Item><Link to="/logout">Wyloguj</Link></Menu.Item>
                            {/*<Menu.Item>Ostatnio licytowane</Menu.Item>*/}
                            {/*<Menu.Item>Zakończone aukcje</Menu.Item>*/}
                            {/*<Menu.Item>Moje konto</Menu.Item>*/}
                        </Menu>
                    </Sider>
                    <Content  style={{minHeight: "100vh"}}>
                            <Outlet />
                    </Content>
                </Layout>
                <Footer>Car Auctions System Developed by Andrzej Połetek</Footer>
            </Layout>
    )
}

export default BaseTemplate;