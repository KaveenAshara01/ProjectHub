import { useAuth } from "../context/AuthContext";

const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-white text-gray-800 p-6">
      <h1 className="text-3xl font-bold mb-4">👤 Member Dashboard</h1>
      <p className="mb-2">Welcome, <span className="font-semibold">{user?.username}</span>!</p>
      <p>Your role is: <span className="text-green-600 font-medium">{user?.role}</span></p>
      <button
        onClick={logout}
        className="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
      >
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
