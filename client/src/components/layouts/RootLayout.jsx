import { Outlet } from "react-router-dom";
import Footer from "./Footer"
import Header from "./Header";

const RootLayout = () => {
    return (
        <>
            <Header />
            <main className="container">
                <article>
                    <Outlet />
                </article>
            </main>
            <Footer />
        </>
    )
}

export default RootLayout