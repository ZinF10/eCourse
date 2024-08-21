import { Link } from 'react-router-dom'

const Logo = ({ type }) => {
    return (
        <Link className={type} to={'/'}>eCourse 🎓</Link>
    )
}

export default Logo