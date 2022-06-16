import React from 'react';
import {Layout, PageHeader, Input, Form, DatePicker, InputNumber, Select, Upload, Button} from 'antd'
import { UploadOutlined } from '@ant-design/icons';



const {Content} = Layout
const {TextArea} = Input;
const {Option} = Select;

const AuctionCreator = () =>{
    let fileList = []
    const [form] = Form.useForm()
    const onFinish = (values) => {
        console.log('Received values of form: ', values);
    };
    return(
        <Content>
            <div className="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
                <PageHeader className="site-page-header" title="Utwórz Aukcje"  subTitle="Utwórz nową aukcje"/>
                <div>
                    <Form onFinish={onFinish} form={form} labelCol={{span: 4}} wrapperCol={{span:14}}>
                        <Form.Item name="auction_title" label="Tytuł aukcji">
                            <Input required={true} id="auction_title" name="auction_title" />
                        </Form.Item>
                        <Form.Item  name="start_date" label="Data rozpoczęcia aukcji">
                            <DatePicker required={true} name="start_date" />
                        </Form.Item>
                        <Form.Item name="finish_date" label="Data zakończenia aukcji">
                            <DatePicker required={true} name="finish_date" />
                        </Form.Item>
                        <Form.Item name="start_price" label="Cena wywoławcza (w PLN)">
                            <InputNumber required={true} required={true} style={{width:"100%"}} step="0.01" min="0" name="start_price" />
                        </Form.Item>
                        <Form.Item name="mileage" label="Przebieg">
                            <InputNumber required={true} step="1" min="0" name="mileage" />
                        </Form.Item>
                        <Form.Item name="engine_power" label="Moc silnika">
                            <InputNumber required={true} step="1" min="0" name="engine_power" />
                        </Form.Item>
                        <Form.Item name="engine_capacity" label="Pojemność silnika (w cm3)">
                            <InputNumber required={true} style={{width:"100%"}} step="1" min="0" name="engine_capacity" />
                        </Form.Item>
                        <Form.Item name="petrol_type" label="Typ paliwa">
                            <Select required={true} name="petrol_type">
                                <Option value="LPG">LPG</Option>
                                <Option value="ELECTRIC">ELEKTRYCZNY</Option>
                                <Option value="PETROL">BENZYNA</Option>
                                <Option value="DIESEL">DIESEL</Option>
                                <Option value="HYBRID">HYBRYDA</Option>
                                <Option value="CNG">CNG</Option>
                            </Select>
                        </Form.Item>
                        <Form.Item name="type_body" label="Rodzaj nadwozia">
                            <Select required={true} name="type_body">
                                <Option value="SEDAN">SEDAN</Option>
                                <Option value="HATCHBACK">HATCHBACK</Option>
                                <Option value="KOMBI">KOMBI</Option>
                            </Select>
                        </Form.Item>
                        <Form.Item label="Rok produkcji" name="production_year">
                            <Select required={true} name="production_year">
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
                        <Form.Item label="Opis pojazdu" name="description">
                            <TextArea required={true} name="description" rows={10} />
                        </Form.Item>
                        <Form.Item label="Dodaj zdjęcia" name="photos">
                            <Upload name="photos"
                                action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                                listType="picture"
                                defaultFileList={[...fileList]}>
                                <Button icon={<UploadOutlined />}>Upload</Button>
                            </Upload>
                        </Form.Item>
                        <Form.Item label=" ">
                            <Button htmlType="submit">Zapisz</Button>
                        </Form.Item>
                    </Form>
                </div>
            </div>
        </Content>
    )
}

export default AuctionCreator