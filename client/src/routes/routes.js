import { lazy } from 'react';

const Home = lazy(() => import('@/pages/Home'));
const Courses = lazy(() => import('@/pages/Courses'));
const Course = lazy(() => import('@/pages/Course'));
const About = lazy(() => import('@/pages/About'));
const SignUp = lazy(() => import('@/pages/SignUp'));
const LogIn = lazy(() => import('@/pages/LogIn'));
const Profile = lazy(() => import('@/pages/Profile'));
const Cart = lazy(() => import('@/pages/Cart'));
const NotFound = lazy(() => import('@/pages/NotFound'));

const PublicRoutes = [
    { path: '/', component: Home },
    { path: '/courses', component: Courses },
    { path: '/courses/:id', component: Course },
    { path: '/about', component: About },
    { path: '/sign-up', component: SignUp },
    { path: '/login', component: LogIn },
    { path: '/cart', component: Cart },
    { path: '*', component: NotFound },
];

const PrivateRoutes = [
    {
        path: '/profile',
        component: Profile
    },
];

export { PublicRoutes, PrivateRoutes };
