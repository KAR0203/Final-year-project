// import { Container } from "react-bootstrap";
// import SignUp from "./SignUp";

// import { Route, Routes } from "react-router-dom";
// import Dashboard from "./Dashboard";
// import Login from "./Login";

// import ForgotPassword from "./ForgotPassword";
// import UpdateProfile from "./UpdateProfile";
// import PrivateRoutes from "./PrivateRoutes";

// function App() {
//   return (
//     <Container
//       className="d-flex align-items-center justify-content-center"
//       style={{ minHeight: "100vh" }}
//     >
//       <div className="w-100" style={{ maxWidth: "400px" }}>
//         <Routes>
//           <Route element={<PrivateRoutes />}>
//             <Route path="/" element={<Dashboard />} />
//           </Route>

//           <Route path="/signup" element={<SignUp />} />
//           <Route path="/login" element={<Login />} />

//           <Route path="/forgot-password" element={<ForgotPassword />} />
//           <Route path="/update-profile" element={<UpdateProfile />} />
//         </Routes>
//       </div>
//     </Container>
//   );
// }

// // export default App;

// import React from "react";
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import { Container } from "react-bootstrap";
// import Login from "./Login";
// import SignUp from "./SignUp";
// // import PrivateRoute from "./PrivateRoute";
// import PrivateRoutes from "./PrivateRoutes";
// import Dashboard from "./Dashboard";
// import ForgotPassword from "./ForgotPassword";
// import UpdateProfile from "./UpdateProfile";

// function App() {
//   return (
//     <Container
//       className="d-flex align-items-center justify-content-center"
//       style={{ minHeight: "100vh" }}
//     >
//       <div className="w-100" style={{ maxWidth: "400px" }}>
//         <Router>
//           <Routes>
//             <PrivateRoutes path="/" element={<Dashboard />} />
//             <Route path="/signup" element={<SignUp />} />
//             <Route path="/login" element={<Login />} />
//             {/* <Route path="/forgot-password" element={<ForgotPassword />} />
//             <Route path="/update-profile" element={<UpdateProfile />} /> */}
//           </Routes>
//         </Router>
//       </div>
//     </Container>
//   );
// }

// export default App;


import React from "react";
import { Container } from "react-bootstrap";
import SignUp from "./SignUp";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"; // Remove this line
import Dashboard from "./Dashboard";
import Login from "./Login";
import ForgotPassword from "./ForgotPassword";
import UpdateProfile from "./UpdateProfile";
import PrivateRoutes from "./PrivateRoutes";

function App() {
  return (
    <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
      <div className="w-100" style={{ maxWidth: "400px" }}>
        {/* Remove the Router component */}
        <Routes>
          <Route element={<PrivateRoutes />}>
            <Route path="/" element={<Dashboard />} />
          </Route>

          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/update-profile" element={<UpdateProfile />} />
        </Routes>
      </div>
    </Container>
  );
}

export default App;
