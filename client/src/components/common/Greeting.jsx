import PropTypes from 'prop-types';

const Greeting = ({ username }) => {
	return <h2>Hi, {username}</h2>;
};

Greeting.propTypes = {
	username: PropTypes.string.isRequired,
};

export default Greeting;
