import React, { useState } from 'react';
import api, { setAuthToken } from '../../api/api';
import { useNavigate } from 'react-router-dom';

export default function Login(){
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [err, setErr] = useState('');
  const nav = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setErr('');
    try {
      const resp = await api.post('auth/token/', { username, password });
      localStorage.setItem('access', resp.data.access);
      localStorage.setItem('refresh', resp.data.refresh);
      setAuthToken(resp.data.access);
      nav('/');
    } catch (error) {
      setErr('Invalid credentials');
    }
  };

  return (
    <div style={{padding:20}}>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div><input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} required/></div>
        <div><input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} required/></div>
        <button type="submit">Login</button>
        {err && <p style={{color:'red'}}>{err}</p>}
      </form>
    </div>
  );
}
