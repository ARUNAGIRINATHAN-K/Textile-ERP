import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/auth/Login';
import Dashboard from './components/dashboard/Dashboard';
import { setAuthToken } from './api/api';

const token = localStorage.getItem('access');
if (token) setAuthToken(token);

function PrivateRoute({ children }) {
  const access = localStorage.getItem('access');
  return access ? children : <Navigate to="/login" replace />;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/" element={<PrivateRoute><Dashboard/></PrivateRoute>} />
      </Routes>
    </BrowserRouter>
  );
}
