import ActivityIndicator from "@/components/common/ActivityIndicator";
import NotFound from "@/components/common/NotFound";
import useAxios from "@/hooks/useAxios";
import endpoints from "@/services/endpoints";
import { useParams } from "react-router-dom";

const Course = () => {
    const { id } = useParams();
    const { data, isLoading, error } = useAxios(endpoints['course'](id))

    if (error) console.error(error)

    return (
        <div style={{ padding: 20 }}>
            {isLoading ? <ActivityIndicator /> : (data ? (<>
                <h3>{data.subject}</h3>
                <p>{data.description}</p>
            </>) : <NotFound />)}
        </div>
    );
}

export default Course