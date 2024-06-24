import AuthContext from "@/hooks/contexts/AuthContext";
import { useContext } from "react";

const Profile = () => {
    const [user] = useContext(AuthContext);

    return (
        <section>
            <h1>Profile</h1>
            {user && (<>
                <h3>
                    {user.last_name} {user.first_name}
                </h3>
                <p>
                    Email: {user.email}
                </p>
            </>)}
        </section>
    );
};

export default Profile;
