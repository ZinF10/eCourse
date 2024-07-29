import RegisterForm from '@/components/common/RegisterForm';
import useDocumentTitle from '@/hooks/customs/useDocumentTitle';

const Register = () => {
	useDocumentTitle('Register - eCourse 🎓');

	return (
		<section>
			<h2>Register</h2>
			<RegisterForm />
		</section>
	);
};

export default Register;
