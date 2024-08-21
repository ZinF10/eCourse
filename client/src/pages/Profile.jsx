import Avatar from "@/components/ui/atoms/Avatar";
import { useCurrentUser } from "@/contexts/AuthContext";
import { formatFullName, formatMoment } from "@/utils/format";
import { Table } from "react-bootstrap";

const Profile = () => {
    const [user] = useCurrentUser();

    return (
        <section>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Avatar</th>
                        <th>Username</th>
                        <th>Full Name</th>
                        <th>Last seen on</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><Avatar user={user} size={80} /></td>
                        <td>{user.username}</td>
                        <td>{formatFullName(user.first_name, user.last_name)}</td>
                        <td>{formatMoment(user.last_seen)}</td>
                    </tr>
                </tbody>
            </Table>
        </section>
    )
}

export default Profile