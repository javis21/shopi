import { Button, Jumbotron, Container, Row, Col, Image } from 'react-bootstrap';
import React from 'react';
import MainLayout from '../layouts/HomeLayout';

import { AiOutlineFire } from 'react-icons/ai';

const Home = () => (
  <MainLayout>
   
  

    <Jumbotron className="bg-light">
      <Container>
        <Row>
          <Col md={6} className="my-auto">
            <h1  style={{color: "white"}}><b >WELCOME TO <p style={{color: "white"}}> SMART FOOD</p> </b></h1>
            <h5 className="mt-4 mb-4"  style={{color: "white"}}> 
              A smart and efficent solution to help restaurents , hotels and cafes share a digital menu with their cusotmers .
          
            </h5>
            <br/>
            <Button href="/places" variant="standard" size="lg" >
              Create Menu
              <AiOutlineFire/>
            </Button>
          </Col>
          <Col md={6}>
            <Image src="smart1.png" rounded fluid  style={{width: "450px"}} />
          </Col>
        </Row>
      </Container>
    </Jumbotron>
  </MainLayout>
);

export default Home;