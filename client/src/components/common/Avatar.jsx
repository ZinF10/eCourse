import { formatFullName } from '@/utils/format';
import { Image } from 'react-bootstrap';

const Avatar = ({ user, size }) => {
    return (
        <Image
            src={`${user.avatar}`}
            roundedCircle width={size}
            height={size}
            alt={formatFullName(user.last_name, user.first_name)}
            title={formatFullName(user.last_name, user.first_name)}
        />
    );
}

export default Avatar