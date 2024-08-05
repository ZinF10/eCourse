import React from 'react'
import { Container, Navbar } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import Navigation from './Navigation'

const Header = () => {
    return (
        <header className='sticky-top shadow-sm'>
            <Navbar collapseOnSelect expand="lg" bg="white" data-bs-theme="white">
                <Container>
                    <Link className="navbar-brand fw-bold fs-3" to={'/'}>eCourse 🎓</Link>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navigation />
                </Container>
            </Navbar>
        </header>
    )
}

export default Header