import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import httpClient from '@/services/client';
import endpoints from '@/services/endpoints';
import { registerSchema } from '@/utils/schemas'

const SignUp = () => {
	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm({
		resolver: yupResolver(registerSchema),
	});

	const onSubmit = async (data) => {
		const formData = new FormData();
		formData.append('username', data.username);
		formData.append('email', data.email);
		formData.append('password', data.password);
		formData.append('first_name', data.firstName);
		formData.append('last_name', data.lastName);
		formData.append('avatar', data.avatar[0]);

		for (let [key, value] of formData.entries()) {
			console.log(`${key}: ${value}`);
		}

		try {
			const response = await httpClient.post(
				endpoints['register'],
				formData,
				{
					headers: {
						'Content-Type': 'multipart/form-data',
					},
				},
			);
			response.data && navigate('/login')
		} catch (error) {
			console.error(error);
		}
	};

	return (
		<section>
			<h2>Sign Up</h2>
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
						name="password"
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
						name="confirmPassword"
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
				<button type='submit'>Sign Up</button>
			</form>
		</section>
	);
};
export default SignUp;