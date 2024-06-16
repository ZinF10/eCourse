import { configureStore } from '@reduxjs/toolkit';
import AuthReducer from './reducers/AuthReducer';

export const store = configureStore({
	reducer: {
		user: AuthReducer,
	},
});
