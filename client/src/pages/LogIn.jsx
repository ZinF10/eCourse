import { Card, CardBody } from "react-bootstrap"
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import useAuth from "@/hooks/useAuth";
import { useNavigate } from "react-router-dom";
import { loginSchema } from "@/utils/schemas";


const LogIn = () => {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(loginSchema),
    });

    const { login, isAuthenticated } = useAuth();
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        const success = await login(data.email, data.password);

        success && (isAuthenticated() ?? navigate('/'))
    };

    return (
        <div>
            <h1>Log In</h1>
            <Card>
                <CardBody>
                    <form onSubmit={handleSubmit(onSubmit)}>
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
                        <button type='submit'>Log In</button>
                    </form>
                </CardBody>
            </Card>
        </div>
    )
}

export default LogIn