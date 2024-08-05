import Avatar from "@/components/common/Avatar";
import { useCurrentUser } from "@/contexts/AuthContext";
import { formatMoment } from "@/utils/format";
import { Table } from "react-bootstrap";

const Profile = () => {
    const [user] = useCurrentUser();

    return (
        <section>
            <Table>
                <thead>
                    <tr>
                        <td><Avatar user={user} size={80} /></td>
                        <td>
                            <h1>Profile: {user.username}</h1>
                            <p>Last seen on: {formatMoment(user.last_seen)}</p>
                        </td>
                    </tr>
                </thead>
            </Table>
            <hr className='divider py-2'></hr>
        </section>
    )
}

export default Profile