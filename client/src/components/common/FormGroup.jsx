import PropTypes from 'prop-types';

const FormGroup = ({ label, type="text", register, name, errors }) => {
    return (
        <div className='form-group'>
            <label>{label}</label>
            <input type={type} {...register(name)} />
            {errors[name] && <span>{errors[name].message}</span>}
        </div>
    );
};

FormGroup.propTypes = {
    label: PropTypes.string.isRequired,
    type: PropTypes.string,
    register: PropTypes.func.isRequired,
    name: PropTypes.string.isRequired,
    errors: PropTypes.object.isRequired,
};

export default FormGroup;