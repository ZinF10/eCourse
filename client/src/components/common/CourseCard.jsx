import { Link } from "react-router-dom"
import PropTypes from 'prop-types';


const CourseCard = ({ item }) => {
    return (
        <>
            <Link
                to={`courses/${item.id}`}>
                {item.subject}
            </Link>
            <p>
                Price: $
                {item.price}
            </p>
            <p>
                Category:{' '}
                <i>
                    {
                        item.category
                    }
                </i>
            </p>
        </>
    )
}

CourseCard.propTypes = {
    item: PropTypes.shape({
        id: PropTypes.number.isRequired,
        subject: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        category: PropTypes.string.isRequired
    }).isRequired
}

export default CourseCard