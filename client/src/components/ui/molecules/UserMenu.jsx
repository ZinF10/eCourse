import { Badge, Nav, NavDropdown } from 'react-bootstrap'
import { CiShoppingCart } from 'react-icons/ci'
import { Link, NavLink } from 'react-router-dom'
import Avatar from './Avatar';
import { useCurrentUser } from '@/contexts/AuthContext';
import useAuth from '@/hooks/useAuth';

const UserMenu = ({ navigate }) => {
    const [user] = useCurrentUser();
    const { logout } = useAuth();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    return (
        <Nav className='align-items-start align-items-lg-center'>
            {user ? (
                <NavDropdown title={<Avatar user={user} size={32} />} id="auth-nav-dropdown" className='mb-2 mb-lg-0'>
                    <NavLink className={'dropdown-item'} to={'/profile'}>
                        Profile
                    </NavLink>
                    <NavDropdown.Divider />
                    <NavDropdown.Item onClick={handleLogout}>Log Out</NavDropdown.Item>
                </NavDropdown>
            ) : (
                <>
                    <Link className={'btn btn-outline-dark me-lg-2 mb-2 mb-lg-0'} to={'/login'}>Log In</Link>
                    <Link className={'btn btn-outline-primary mb-2 mb-lg-0 fw-bold'} to={'/sign-up'}>
                        Join for free
                    </Link>
                </>)}
            <NavLink className={'nav-link px-2'} to={'/cart'}>
                <div className="position-relative">
                    <CiShoppingCart size={24} />
                    <Badge bg="body-secondary" className="position-absolute top-0 start-100 text-dark translate-middle badge rounded-pill">
                        0
                        <span className="visually-hidden">unread messages</span>
                    </Badge>
                </div>
            </NavLink>
        </Nav>
    )
}

export default UserMenu