import React from 'react';
import {Layout, PageHeader, Input, Form, DatePicker, InputNumber, Select, Upload, Button} from 'antd'
import { UploadOutlined } from '@ant-design/icons';



const {Content} = Layout
const {TextArea} = Input;
const {Option} = Select;

const AuctionCreator = () =>{
    let fileList = []
    return(
        <Content>
            <div className="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
                <PageHeader className="site-page-header" title="Utwórz Aukcje"  subTitle="Utwórz nową aukcje"/>
                <div>
                    <Form labelCol={{span: 4}} wrapperCol={{span:14}}>
                        <Form.Item label="Tytuł aukcji">
                            <Input />
                        </Form.Item>
                        <Form.Item label="Data rozpoczęcia aukcji">
                            <DatePicker />
                        </Form.Item>
                        <Form.Item label="Data zakończenia aukcji">
                            <DatePicker />
                        </Form.Item>
                        <Form.Item label="Cena wywoławcza">
                            <InputNumber step="0.01" min="0" /> PLN
                        </Form.Item>
                        <Form.Item label="Rok produkcji">
                            <Select>
                                <Option value="1990">1990</Option>
                                <Option value="1991">1991</Option>
                                <Option value="1992">1992</Option>
                                <Option value="1993">1993</Option>
                                <Option value="1994">1994</Option>
                                <Option value="1995">1995</Option>
                                <Option value="1996">1996</Option>
                                <Option value="1997">1997</Option>
                                <Option value="1998">1998</Option>
                                <Option value="1999">1999</Option>
                                <Option value="2000">2000</Option>
                                <Option value="2001">2001</Option>
                                <Option value="2002">2002</Option>
                                <Option value="2003">2003</Option>
                                <Option value="2004">2004</Option>
                                <Option value="2005">2005</Option>
                                <Option value="2006">2006</Option>
                                <Option value="2007">2007</Option>
                                <Option value="2008">2008</Option>
                                <Option value="2009">2009</Option>
                                <Option value="2010">2010</Option>
                                <Option value="2011">2011</Option>
                                <Option value="2012">2012</Option>
                                <Option value="2013">2013</Option>
                                <Option value="2014">2014</Option>
                                <Option value="2015">2015</Option>
                                <Option value="2016">2016</Option>
                                <Option value="2017">2017</Option>
                                <Option value="2018">2018</Option>
                                <Option value="2019">2019</Option>
                                <Option value="2020">2020</Option>
                                <Option value="2021">2021</Option>
                                <Option value="2022">2022</Option>
                            </Select>
                        </Form.Item>
                        <Form.Item label="Opis pojazdu">
                            <TextArea rows={10} />
                        </Form.Item>
                        <Form.Item label="Dodaj zdjęcia">
                        <Upload
                            action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                            listType="picture"
                            defaultFileList={[...fileList]}>
                            <Button icon={<UploadOutlined />}>Upload</Button>
                        </Upload>
                        </Form.Item>
                        <Form.Item label=" ">
                            <Button>Zapisz</Button>
                        </Form.Item>
                    </Form>
                </div>
            </div>
        </Content>
    )
}

export default AuctionCreator