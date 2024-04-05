// import { Outlet, Navigate } from "react-router-dom";
// import { useAuth } from "../contexts/AuthContext";

// const PrivateRoutes = () => {
//   const { currentUser } = useAuth();

//   return currentUser ? <Outlet /> : <Navigate to="/login" />;
// };

// export default PrivateRoutes;

// import React from "react";
// import { Route, Navigate } from "react-router-dom";
// import { useAuth } from "../contexts/AuthContext";

// export default function PrivateRoute({ element, ...rest }) {
//   const { currentUser } = useAuth();

//   return <Route {...rest} element={currentUser ? element : <Navigate to="/login" />} />;
// }


import { Outlet, Navigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

const PrivateRoutes = () => {
  const { currentUser } = useAuth();

  return currentUser ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoutes;
