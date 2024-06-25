import Loading from "@/components/common/Loading";
import useFetch from "@/hooks/customs/useFetch";
import endpoints from "@/services/endpoints";
import { useParams } from "react-router-dom";

const LessonDetail = () => {
    const { lesson_id } = useParams();

    const { data: detail, isLoading, error } = useFetch(
        endpoints['lesson_detail'](lesson_id),
    );

    if (isLoading) {
        return <Loading />;
    }

    if (error) {
        return <p>{error}</p>;
    }


    return (
        <section>
            <h1>Lesson Detail</h1>
            {detail ? (
                <>
                    <ul>
                        <li>Title: {detail.subject}</li>
                        <li>Content: {detail.content}</li>
                    </ul>
                </>
            ) : (
                <p>No items</p>
            )}
        </section>
    )
}

export default LessonDetail