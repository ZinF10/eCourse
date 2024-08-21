import { Nav, NavDropdown } from 'react-bootstrap'
import { Link, NavLink } from 'react-router-dom'
import ActivityIndicator from '../atoms/ActivityIndicator'
import useAxios from '@/hooks/useAxios'
import endpoints from '@/services/endpoints'

const NavigationMenu = () => {
    const { data, isLoading } = useAxios(endpoints['categories'])

    return (
        <Nav className="me-lg-auto mb-2 mb-md-0">
            <NavDropdown title="Categories" id="basic-nav-dropdown">
                {isLoading ? (
                    <Link className={'dropdown-item'} to={'#'}>
                        <ActivityIndicator />
                    </Link>
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
    )
}

export default NavigationMenu