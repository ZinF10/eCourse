import { Spinner } from "react-bootstrap"

const ActivityIndicator = () => {
    return (
        <div>
            <Spinner animation="border" role="status" size="sm">
                <span className="visually-hidden">Loading...</span>
            </Spinner> Loading, please wait...
        </div>
    )
}

export default ActivityIndicator