import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import axiosInstance from '@/services/APIs';
import endpoints from '@/services/endpoints';

const schema = yup
	.object()
	.shape({
		username: yup.string().required('Username is required'),
		email: yup
			.string()
			.email('Invalid email')
			.required('Email is required'),
		password: yup
			.string()
			.required('Password is required')
			.min(6, 'Password must be at least 6 characters'),
		confirmPassword: yup
			.string()
			.oneOf(
				[yup.ref('password'), null],
				'Passwords must match',
			),
		firstName: yup.string().required('First Name is required'),
		lastName: yup.string().required('Last Name is required'),
		avatar: yup.mixed(),
	})
	.required();

const Register = () => {
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
						'Content-Type':
							'multipart/form-data',
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
		<section>
			<h2>Register</h2>
			<form onSubmit={handleSubmit(onSubmit)}>
				<div className='form-group'>
					<label>Username</label>
					<input
						type='text'
						{...register('username')}
					/>
					{errors.username && (
						<span>
							{
								errors.username
									.message
							}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Email</label>
					<input
						type='email'
						{...register('email')}
					/>
					{errors.email && (
						<span>
							{errors.email.message}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Password</label>
					<input
						type='password'
						{...register('password')}
					/>
					{errors.password && (
						<span>
							{
								errors.password
									.message
							}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Confirm Password</label>
					<input
						type='password'
						{...register('confirmPassword')}
					/>
					{errors.confirmPassword && (
						<span>
							{
								errors
									.confirmPassword
									.message
							}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>First Name</label>
					<input
						type='text'
						{...register('firstName')}
					/>
					{errors.firstName && (
						<span>
							{
								errors.firstName
									.message
							}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Last Name</label>
					<input
						type='text'
						{...register('lastName')}
					/>
					{errors.lastName && (
						<span>
							{
								errors.lastName
									.message
							}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Avatar</label>
					<input
						type='file'
						{...register('avatar')}
					/>
					{errors.avatar && (
						<span>
							{errors.avatar.message}
						</span>
					)}
				</div>
				<button type='submit'>Register</button>
			</form>
		</section>
	);
};

export default Register;
