import * as yup from 'yup';

const RegisterSchema = yup
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

export { RegisterSchema }