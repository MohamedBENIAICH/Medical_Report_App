import React, { createContext, useState, useEffect, useContext } from "react";
import axios from "../config/axios";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("authToken");
    if (token) {
      checkTokenValidity(token);
    } else {
      setLoading(false);
    }
  }, []);

  const checkTokenValidity = async (token) => {
    try {
      const response = await axios.post(
        "/api/auth/verify-token/",
        {},
        { headers: { Authorization: `Token ${token}` } }
      );

      if (response.data.valid) {
        setCurrentUser(response.data.user);
      } else {
        localStorage.removeItem("authToken");
      }
    } catch (error) {
      localStorage.removeItem("authToken");
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    try {
      const response = await axios.post("/api/auth/login/", {
        email,
        password,
      });
      localStorage.setItem("authToken", response.data.token);
      setCurrentUser(response.data.user);
      setError("");
      return response.data;
    } catch (error) {
      const errorMsg = error.response?.data?.error || "Login failed";
      setError(errorMsg);
      throw new Error(errorMsg);
    }
  };

  const signup = async (userData) => {
    try {
      const response = await axios.post("/api/auth/register/", userData);
      localStorage.setItem("authToken", response.data.token);
      setCurrentUser(response.data.user);
      setError("");
      return response.data;
    } catch (error) {
      const errorMsg = error.response?.data?.message || "Signup failed";
      setError(errorMsg);
      throw new Error(errorMsg);
    }
  };

  const googleAuth = async (tokenId) => {
    try {
      const response = await axios.post("/api/auth/google/", {
        token_id: tokenId,
      });
      localStorage.setItem("authToken", response.data.token);
      setCurrentUser(response.data.user);
      setError("");
      return response.data;
    } catch (error) {
      const errorMsg =
        error.response?.data?.message || "Google authentication failed";
      setError(errorMsg);
      throw new Error(errorMsg);
    }
  };

  const resetPassword = async (email) => {
    try {
      await axios.post("/api/auth/reset-password/", { email });
      setError("");
      return true;
    } catch (error) {
      const errorMsg = error.response?.data?.message || "Password reset failed";
      setError(errorMsg);
      throw new Error(errorMsg);
    }
  };

  const logout = () => {
    localStorage.removeItem("authToken");
    setCurrentUser(null);
  };

  const value = {
    currentUser,
    login,
    signup,
    googleAuth,
    resetPassword,
    logout,
    error,
    loading,
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
};
