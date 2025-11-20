import React from 'react';
import api from '../../api/api';

export default function Dashboard(){
  const logout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    window.location.href = '/login';
  };

  return (
    <div style={{padding:20}}>
      <h1>Textile ERP Dashboard</h1>
      <p>Welcome. Use menu to navigate modules (Procurement, Inventory, Production, Quality, Sales)</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
