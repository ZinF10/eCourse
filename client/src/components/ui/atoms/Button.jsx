import { Button as BootrapButton } from "react-bootstrap";

const Button = ({ children, onClick, variant, type = 'button' }) => {
    return (
        <BootrapButton type={type} onClick={onClick} variant={variant}>
            {children}
        </BootrapButton>
    );
};

export default Button