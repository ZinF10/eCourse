import Each from "../common/Each";
import CourseCard from "../common/CourseCard";
import PropTypes from 'prop-types';

const CourseList = ({ courses }) => {
    return (
        <>
            {courses ? (
                <section className="flex">
                    <Each
                        of={courses}
                        render={(item, index) => (
                            <CourseCard item={item} key={index} />
                        )}
                    />
                </section>
            ) : (
                <p>No items exists</p>
            )}
        </>
    )
}

CourseList.propTypes = {
    courses: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            subject: PropTypes.string.isRequired,
            image: PropTypes.string,
            price: PropTypes.number.isRequired,
            date_created: PropTypes.string.isRequired
        })
    ).isRequired,
};

export default CourseList