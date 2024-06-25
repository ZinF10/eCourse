import useFetch from "@/hooks/customs/useFetch";
import endpoints from "@/services/endpoints";
import Loading from "../common/Loading";
import Each from "../common/Each";
import CourseCard from "../common/CourseCard";

const CourseList = () => {
    const { data, isLoading, error } = useFetch(endpoints['courses']());

    if (isLoading) {
        return <Loading />;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <>
            {data ? (
                <Each
                    of={data}
                    render={(item, index) => (
                        <section key={index}>
                            <CourseCard item={item} />
                        </section>
                    )}
                />
            ) : (
                <p>No items exists</p>
            )}
        </>
    )
}

export default CourseList