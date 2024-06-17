import React from "react";
import { Route, Routes } from "react-router-dom";
import ProtectedRoute from "./routes/ProtectedRoute";
import Home from "./pages/Home";
import Registration from "./pages/Registration";
import Login from "./pages/Login";
import Bio from "./pages/Bio";
import Comment from "./pages/Comment"

function App() {
  return (
    <Routes>
      <Route path="/register/" element={<Registration />} />
      <Route path="/login/" element={<Login />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        }
      />
      <Route path="/login/" element={<div>Login</div>} />
      <Route path="/profile/" element={<Bio />} />
      <Route path="/comment/" element={<Comment />} />
    </Routes>
  );
}
export default App;
