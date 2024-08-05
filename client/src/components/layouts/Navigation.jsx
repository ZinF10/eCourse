import useAxios from "@/hooks/useAxios"
import endpoints from "@/services/endpoints"
import { Badge, Form, Nav, Navbar, NavDropdown } from "react-bootstrap"
import { Link, NavLink, useNavigate } from "react-router-dom"
import ActivityIndicator from "../common/ActivityIndicator"
import { useCurrentUser } from "@/contexts/AuthContext"
import Avatar from "../common/Avatar"
import useAuth from "@/hooks/useAuth"
import { CiShoppingCart } from "react-icons/ci";

const Navigation = () => {
    const [user] = useCurrentUser();
    const { logout } = useAuth();
    const { data, isLoading } = useAxios(endpoints['categories'])
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        let params = serializeFormQuery(event.target);
        navigate(`courses?${params}`);
    };

    const serializeFormQuery = (form) => {
        const formData = new FormData(form);
        let params = new URLSearchParams();
        for (let [key, value] of formData.entries()) {
            params.append(key, value);
        }
        return params.toString();
    };

    return (
        <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-lg-auto mb-2 mb-md-0">
                <NavDropdown title="Categories" id="basic-nav-dropdown">
                    {isLoading ? (
                        <ActivityIndicator />
                    ) : (
                        data && data.length > 0 && data.map((category) => (
                            <Link className={'dropdown-item'} key={category.id} to={`/courses?category=${category.id}`}>
                                {category.name}
                            </Link>
                        ))
                    )}
                </NavDropdown>
                <NavLink className={'nav-link'} to={'/courses'}>Courses</NavLink>
                <NavLink className={'nav-link'} to="/about">
                    About
                </NavLink>
            </Nav>
            <Form className="d-flex mb-3 mb-lg-0 me-lg-3" onSubmit={handleSubmit}>
                <Form.Control
                    type="search"
                    placeholder="Search for anything"
                    aria-label="Search for anything"
                    name='keyword'
                />
            </Form>
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
                        <NavLink className={'btn btn-outline-dark me-lg-2 mb-2 mb-lg-0'} to={'/login'}>Log In</NavLink>
                        <NavLink className={'btn btn-outline-primary mb-2 mb-lg-0 fw-bold'} to={'/sign-up'}>
                            Join for free
                        </NavLink>
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
        </Navbar.Collapse>
    )
}

export default Navigation