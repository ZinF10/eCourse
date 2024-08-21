import { Container, Navbar } from 'react-bootstrap'
import Logo from '../molecules/Logo'
import SearchBar from '../molecules/SearchBar'
import UserMenu from '../molecules/UserMenu'
import { useNavigate } from 'react-router-dom'
import NavigationMenu from '../molecules/NavigationMenu'

const Header = () => {
    const navigate = useNavigate();

    return (
        <header className='sticky-top shadow-sm'>
            <Navbar collapseOnSelect expand="lg" bg="white" data-bs-theme="white">
                <Container>
                    <Logo type="navbar-brand fw-bold fs-3" />
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <NavigationMenu />
                        <SearchBar navigate={navigate} />
                        <UserMenu navigate={navigate} />
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    )
}

export default Header