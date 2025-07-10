import { Link } from "react-router-dom";

const Unauthorized = () => {
  return (
    <div className="h-screen flex flex-col items-center justify-center bg-gray-100 text-center p-6">
      <h1 className="text-4xl font-bold text-red-600 mb-4">403 - Unauthorized</h1>
      <p className="text-lg text-gray-700 mb-6">You don't have permission to view this page.</p>
      <Link to="/login" className="text-blue-600 underline hover:text-blue-800">
        Go back to login
      </Link>
    </div>
  );
};

export default Unauthorized;
