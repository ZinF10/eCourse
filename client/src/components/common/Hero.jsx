import { Link } from "react-router-dom"

const Hero = () => {
    return (
        <div className={"px-4 py-5 my-5 text-center"}>
            <h1 className={"display-5 fw-bold text-body-emphasis"}>Welcome to eCourse 🎓 System</h1>
            <div className={"col-lg-6 mx-auto"}>
                <h3 className={"lead mb-2 fs-3 fw-bold"}>Jump into learning for less</h3>
                <p className={"lead mb-4"}>If you're new to Udemy, we've got good news: For a limited time, courses start at just ₫299,000 for new learners! Shop now.</p>
                <div className={"d-grid gap-2 d-sm-flex justify-content-sm-center"}>
                    <Link className={'btn btn-lg btn-primary me-lg-2 fw-bold'} to={'/orders'}>Start 7-days free trial</Link>
                    <Link className={'btn btn-lg btn-outline-primary fw-bold'} to={'/sign-up'}>Join for free</Link>
                </div>
            </div>
        </div>
    )
}

export default Hero