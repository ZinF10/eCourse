import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';
import { config as dotenvConfig } from 'dotenv';

// run package config
dotenvConfig();

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],
	resolve: {
		alias: {
			// eslint-disable-next-line no-undef
			'@': path.resolve(__dirname, './src/'),
		},
	},
	// define .env
	define: {
		// eslint-disable-next-line no-undef
		'process.env': process.env,
	},
});
