import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import axiosInstance from '@/services/APIs';
import endpoints from '@/services/endpoints';
import FormGroup from './FormGroup';

const schema = yup.object().shape({
    username: yup.string().required('Username is required'),
    email: yup.string().email('Invalid email').required('Email is required'),
    password: yup
        .string()
        .required('Password is required')
        .min(6, 'Password must be at least 6 characters'),
    confirmPassword: yup
        .string()
        .oneOf([yup.ref('password'), null], 'Passwords must match')
        .required('Confirm Password is required'),
    firstName: yup.string().required('First Name is required'),
    lastName: yup.string().required('Last Name is required'),
    avatar: yup.mixed(),
}).required();

const RegisterForm = () => {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = async (data) => {
        const formData = new FormData();
        formData.append('username', data.username);
        formData.append('email', data.email);
        formData.append('password', data.password);
        formData.append('first_name', data.firstName);
        formData.append('last_name', data.lastName);
        formData.append('avatar', data.avatar[0]);

        try {
            const response = await axiosInstance.post(
                endpoints['register'],
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                },
            );
            console.log(response.data);
            alert('Registration successful');
        } catch (error) {
            console.error(error);
            alert('Registration failed');
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <FormGroup label="Username" register={register} name="username" errors={errors} />
            <FormGroup label="Email" type="email" register={register} name="email" errors={errors} />
            <FormGroup label="Password" type="password" register={register} name="password" errors={errors} />
            <FormGroup label="Confirm Password" type="password" register={register} name="confirmPassword" errors={errors} />
            <FormGroup label="First Name" register={register} name="firstName" errors={errors} />
            <FormGroup label="Last Name" register={register} name="lastName" errors={errors} />
            <div className='form-group'>
                <label>Avatar</label>
                <input type='file' {...register('avatar')} />
                {errors.avatar && <span>{errors.avatar.message}</span>}
            </div>
            <button type='submit'>Register</button>
        </form>
    );
};

export default RegisterForm;