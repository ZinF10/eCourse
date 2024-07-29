import { Children } from 'react';

const Each = ({ render, of }) =>
	Children.toArray(of.map((item, index) => render(item, index)));

export default Each;