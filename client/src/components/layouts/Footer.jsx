import { Button, Col, Container, Form, Row } from "react-bootstrap"
import { Link, NavLink } from "react-router-dom"
import { CiFacebook, CiInstagram, CiTwitter } from "react-icons/ci";

const Footer = () => {
    return (
        <footer className="py-5 bg-body-tertiary">
            <Container>
                <Row>
                    <Col xs={12} md={4} className="mb-3">
                        <NavLink to={"/"} className="navbar-brand fw-bold fs-3 d-flex align-items-center mb-3 link-body-emphasis text-decoration-none">
                            eCourse 🎓
                        </NavLink>
                        <p className='text-body-tertiary' style={{ textAlign: 'justify' }}><strong className="text-dark">eCourse</strong> is a leading online learning platform with thousands of high-quality courses. We are committed to providing the best learning experience for our students.</p>
                    </Col>

                    <Col xs={4} md={2} className="mb-3">
                        <h5>eCourse 🎓</h5>
                        <ul className="nav flex-column">
                            <li className="nav-item mb-2">
                                <NavLink className='nav-link p-0 text-body-secondary' to={'/'}>Home</NavLink>
                            </li>
                            <li className="nav-item mb-2">
                                <NavLink className='nav-link p-0 text-body-secondary' to={'/courses'}>Courses</NavLink>
                            </li>
                            <li className="nav-item mb-2">
                                <NavLink className='nav-link p-0 text-body-secondary' to={'/about'}>About</NavLink>
                            </li>
                        </ul>
                    </Col>

                    <Col xs={12} md={5} className="offset-md-1 mb-3">
                        <Form>
                            <h5>Subscribe to our newsletter</h5>
                            <p>Monthly digest of what's new and exciting from us.</p>
                            <div className="d-flex flex-column flex-sm-row w-100 gap-2">
                                <Form.Control type="email" placeholder="Enter email" />
                                <Button variant="outline-primary" className='fw-bold' type="submit">Subscribe</Button>
                            </div>
                        </Form>
                    </Col>
                </Row>
                <div className="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
                    <p className="text-body-secondary">
                        &copy; {new Date().getFullYear()} eCourse Inc. All rights reserved.
                    </p>
                    <ul className="list-unstyled d-flex">
                        <li className="ms-3"><Link className="link-body-emphasis" to={''} target="_blank"><CiFacebook size={32} /></Link></li>
                        <li className="ms-3"><Link className="link-body-emphasis" to={''} target="_blank"><CiInstagram size={32} /></Link></li>
                        <li className="ms-3"><Link className="link-body-emphasis" to={''} target="_blank"><CiTwitter size={32} /></Link></li>
                    </ul>
                </div>
            </Container>
        </footer>
    )
}

export default Footer