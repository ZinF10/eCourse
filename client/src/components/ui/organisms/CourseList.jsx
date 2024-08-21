import useAxios from "@/hooks/useAxios";
import endpoints from "@/services/endpoints";
import { useLocation } from "react-router-dom";
import { Row } from "react-bootstrap";
import ActivityIndicator from "../atoms/ActivityIndicator";
import NoMatch from "../atoms/NoMatch";
import Item from "../atoms/Item";

const CourseList = ({ isNew }) => {
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const category = queryParams.get('category');
    const keyword = queryParams.get('keyword');
    const latest = queryParams.get('latest') || isNew;
    const { data, isLoading, error } = useAxios(endpoints['courses'](keyword, category, latest))

    if (error) return <p>{error}</p>;

    return (
        <Row className="g-4">
            {isLoading ? <ActivityIndicator /> : (data && data.length > 0 ? (data.map((course) => (
                <Item key={course.id} course={course} />
            ))) : <NoMatch />)}
        </Row>
    )
}

export default CourseList