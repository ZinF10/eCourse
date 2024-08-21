import { Outlet } from "react-router-dom";
import Footer from "../ui/organisms/Footer"
import Header from "../ui/organisms/Header";

const RootLayout = () => {
    return (
        <>
            <Header />
            <main className="container">
                <Outlet />
            </main>
            <Footer />
        </>
    )
}

export default RootLayout