// import React, { useRef, useState } from "react";
// import { Form, Button, Card, Alert } from "react-bootstrap";
// import { Link, useNavigate } from "react-router-dom";
// import { useAuth } from "../contexts/AuthContext";

// export default function Login() {
//   const emailRef = useRef();
//   const passwordRef = useRef();

//   const { login } = useAuth();
//   const [error, setError] = useState("");
//   const [loading, setLoading] = useState(false);
//   const navigate = useNavigate();

//   async function handleSubmit(e) {
//     e.preventDefault();

//     try {
//       setError("");
//       setLoading(true);
//       await login(emailRef.current.value, passwordRef.current.value);
//       navigate("/");
//     } catch {
//       setError("Failed to Login");
//     }
//     setLoading(false);
//   }

//   return (
//     <>
//       <Card>
//         <Card.Body>
//           <h2 className="text-center mb-4">Log In</h2>
//           {/* {currentUser.email} */}
//           {error && <Alert variant="danger">{error}</Alert>}
//           <Form onSubmit={handleSubmit}>
//             <Form.Group id="email">
//               <Form.Label>Email</Form.Label>
//               <Form.Control type="email" ref={emailRef} required />
//             </Form.Group>
//             <Form.Group id="password">
//               <Form.Label>Password</Form.Label>
//               <Form.Control type="password" ref={passwordRef} required />
//             </Form.Group>

//             <Button disabled={loading} className="w-100 mt-3" type="submit">
//               Login
//             </Button>
//           </Form>

//           <div className="w-100 text-center mt-3">
//             <Link to="/forgot-password">Forget Password?</Link>
//           </div>
//         </Card.Body>
//       </Card>

//       <div className="w-100 text-center mt-2">
//         Need an account ? <Link to="/signup">Sign Up</Link>
//       </div>
//     </>
//   );
// }


// Login.js

// import React, { useRef, useState } from "react";
// import { Form, Button, Card, Alert } from "react-bootstrap";
// import { Link, useHistory } from "react-router-dom";
// import { useAuth } from "../contexts/AuthContext";

// export default function Login() {
//   const emailRef = useRef();
//   const passwordRef = useRef();
//   const { login } = useAuth();
//   const [error, setError] = useState("");
//   const [loading, setLoading] = useState(false);
//   // const history = useHistory();

//   // async function handleSubmit(e) {
//   //   e.preventDefault();
//   //   try {
//   //     setError("");
//   //     setLoading(true);
//   //     await login(emailRef.current.value, passwordRef.current.value);
//   //     history.push("/streamlit?loggedIn=true");
//   //   } catch {
//   //     setError("Failed to Login");
//   //   }
//   //   setLoading(false);
//   // }
//   async function handleSubmit(e) {
//     e.preventDefault();
//     try {
//       setError("");
//       setLoading(true);
//       await login(emailRef.current.value, passwordRef.current.value);
//       window.location.href = "http://yourflaskserverurl:5000/streamlit?loggedIn=true";
//     } catch {
//       setError("Failed to Login");
//     }
//     setLoading(false);
//   }
  

//   return (
//     <>
//       <Card>
//         <Card.Body>
//           <h2 className="text-center mb-4">Log In</h2>
//           {error && <Alert variant="danger">{error}</Alert>}
//           <Form onSubmit={handleSubmit}>
//             <Form.Group id="email">
//               <Form.Label>Email</Form.Label>
//               <Form.Control type="email" ref={emailRef} required />
//             </Form.Group>
//             <Form.Group id="password">
//               <Form.Label>Password</Form.Label>
//               <Form.Control type="password" ref={passwordRef} required />
//             </Form.Group>
//             <Button disabled={loading} className="w-100 mt-3" type="submit">
//               Login
//             </Button>
//           </Form>
//           <div className="w-100 text-center mt-3">
//             <Link to="/forgot-password">Forget Password?</Link>
//           </div>
//         </Card.Body>
//       </Card>
//       <div className="w-100 text-center mt-2">
//         Need an account? <Link to="/signup">Sign Up</Link>
//       </div>
//     </>
//   );
// }


import React, { useRef, useState } from "react";
import { Form, Button, Card, Alert } from "react-bootstrap";
import { useAuth } from "../contexts/AuthContext";
import { Link, useNavigate } from "react-router-dom";

export default function Login() {
  const emailRef = useRef();
  const passwordRef = useRef();
  const { login } = useAuth();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  // const navigate = useNavigate();

  // async function handleSubmit(e) {
  //   e.preventDefault();

  //   try {
  //     setError("");
  //     setLoading(true);
  //     await login(emailRef.current.value, passwordRef.current.value);
  //     // navigate("/");
  //     window.location.href = "http://yourflaskserverurl:5000/streamlit?loggedIn=true";
  //   } catch {
  //     setError("Failed to Login");
  //   }
  //   setLoading(false);
  // }

  async function handleSubmit(e) {
    e.preventDefault();
  
    try {
      setError("");
      setLoading(true);
      await login(emailRef.current.value, passwordRef.current.value);
      // window.location.href = "http://localhost:5000/streamlit?loggedIn=true";
      window.location.href = "http://localhost:8501/streamlit?loggedIn=true";
    } catch {
      setError("Failed to Login");
    }
    setLoading(false);
  }
  

  return (
    <>
      <Card>
        <Card.Body>
          <h2 className="text-center mb-4">Log In</h2>
          {error && <Alert variant="danger">{error}</Alert>}
          <Form onSubmit={handleSubmit}>
            <Form.Group id="email">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" ref={emailRef} required />
            </Form.Group>
            <Form.Group id="password">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" ref={passwordRef} required />
            </Form.Group>
            <Button disabled={loading} className="w-100 mt-3" type="submit">
              Log In
            </Button>
          </Form>
          <div className="w-100 text-center mt-3">
            <Link to="/forgot-password">Forgot Password?</Link>
          </div>
        </Card.Body>
      </Card>
      <div className="w-100 text-center mt-2">
        Need an account? <Link to="/signup">Sign Up</Link>
      </div>
    </>
  );
}

